from django.core import serializers

# from models import User
from django.apps import apps 

from apps.a1crud import models

from ultil.u1core import GenSourceCore 
core_gen = GenSourceCore()

class GenSourceFrontend:
    def __init__(self):
        self.root_link = 'output/'
        self.templates_link = 'templates/'
        
    
    def gen_frontend_angular(self, idproject):
        project_name = models.Project.objects.filter(id = idproject)[0].name

        # copy sample to output
        core_gen.copy_folder('frontend/angular', project_name + '/frontend')

        tables = models.Class.objects.filter(idproject = idproject) 
        
        if len(tables) > 0: 
            content = ''
            html_menu = ''
            param_permision_menu = ''
            load_permision_menu = ''
            content_module = ''

            roles = ''
            permission = ''

            ans = 1
            # print(serializers.serialize("json",  tables))
            for table in tables:  
                classname = table.classname
                properties = table.properties.split(',')
                attributes = table.attributes.split(',')
                lengths = table.lengths.split(',')
                print(classname)
                print(properties) #id,name,address
                print(attributes) #INT,VARCHAR,VARCHAR
                print(lengths)    #0,255,0

                # create item left menu
                html_menu =  html_menu + '            <!--'+ 'c' + str(ans + 1) + '-' + classname +' -->                                                                   \n'
                html_menu =  html_menu + '            <li class="nav-item" *ngIf="isPermissionMenu' + str(ans + 1) + '" (click)="onToggleButtonMobileClick()">  \n'
                html_menu =  html_menu + '              <a class="nav-link" routerLinkActive="active"  \n'
                html_menu =  html_menu + '                routerLink="/manager/'+ 'c' + str(ans + 1) + '-' + classname +'">                                                 \n'
                html_menu =  html_menu + '                <i class="icon-grid menu-icon"></i>                                           \n'
                html_menu =  html_menu + '                <span class="menu-title" i18n>Quản lý ' + classname + '</span>                                   \n'
                html_menu =  html_menu + '              </a>                                                                            \n'
                html_menu =  html_menu + '            </li>                                                                             \n\n'
                
                # create variable permission menu
                param_permision_menu = param_permision_menu + '  isPermissionMenu' + str(ans + 1) + ': boolean = false;\n'

                # create update permission menu
                load_permision_menu = load_permision_menu + '    if (this.staff.role.search(\'' + chr(97 + ans) + ':1\') < 0) { \n'
                load_permision_menu = load_permision_menu + '      this.isPermissionMenu' + str(ans + 1) + ' = true;\n'
                load_permision_menu = load_permision_menu + '    }                                      \n\n'

                # create content module 
                content_module = content_module + '          {                                                               \n'
                content_module = content_module + '            path: \'c'+  str(ans+1) +'-'+classname+'\',                                               \n'
                content_module = content_module + '            loadChildren: () =>                                           \n'
                name_folder_module = 'c'+  str(ans+1) +'-' + classname
                name_module = 'C'+  str(ans+1) +'' + classname.capitalize()
                content_module = content_module + '              import(\'./'+ name_folder_module +'/'+ name_folder_module +'.module\').then((m) => m.'+ name_module +'Module), \n'
                content_module = content_module + '          },                                          \n'  

                # create main module
                # create folder
                component_name = 'c' + str(ans+1) + '-' + classname
                module_path_template = '/frontend/angular/src/app/home-page/content/'
                module_path = project_name + '/frontend/src/app/home-page/content/'
                core_gen.create_folder(module_path + component_name)


                # dialog
                # load data crud for insert and update
                crud = models.CRUD.objects.filter(idproject=idproject, idclass=table.id, actiontype=1)
                if len(crud) > 0:
                    crud = crud[0]
                    c_titles = crud.titles.split(',')
                    c_properties = crud.properties.split(',')
                    c_alias = crud.alias.split(',')
                    c_refers = crud.refers.split(',')
                    c_inputtypes = crud.inputtypes.split(',')
                    c_validates = crud.validates.split(',')
                    c_formats = crud.formats.split(',')

                    params = []
                    param = ''
                    params.append(crud.titlecreate)

                    # add dialog controls
                    for index in range(len(c_properties)):
                        param = param + '        <!-- '+c_properties[index]+' field -->                                                           \n'
                        param = param + '        <div class="col-md-12">                                                       \n'

                        # check control is varchar
                        if c_inputtypes[index] == 'varchar':
                            param = param + '          <mat-form-field class="example-full-width">                                 \n'
                            param = param + '            <mat-label i18n>'+c_titles[index]+' <span class="text-red">*</span></mat-label>           \n'
                            param = param + '            <input matInput [(ngModel)]="input.'+c_properties[index]+'" formControlName="'+c_properties[index]+'">          \n'
                            param = param + '            <button mat-button *ngIf="input.'+c_properties[index]+'" matSuffix mat-icon-button           \n'
                            param = param + '             aria-label="Clear" (click)="input.'+c_properties[index]+'=\'\'">                            \n'
                            param = param + '              <mat-icon>close</mat-icon>                                              \n'
                            param = param + '            </button>                                                                 \n'
                            param = param + '          </mat-form-field>                                                           \n'

                        # check control is date or datetime
                        if c_inputtypes[index] == 'date' or c_inputtypes[index] == 'datetime':
                            param = param + '          <mat-form-field class="example-full-width" appearance="fill">                                   \n'
                            param = param + '            <mat-label i18n>'+c_titles[index]+'<span class="text-red">*</span></mat-label>                          \n'
                            param = param + '            <input matInput [(ngModel)]="input.'+c_properties[index]+'" formControlName="'+c_properties[index]+'" [matDatepicker]="picker'+c_properties[index]+'"> \n'
                            param = param + '            <mat-datepicker-toggle matSuffix [for]="picker'+c_properties[index]+'"></mat-datepicker-toggle>                  \n'
                            param = param + '            <mat-datepicker touchUi #picker'+c_properties[index]+'></mat-datepicker>                                         \n'
                            param = param + '          </mat-form-field>                                                                               \n'

                        # check control is text
                        if c_inputtypes[index] == 'ckeditor':
                            param = param + '          <mat-label i18n>'+c_titles[index]+'<span class="text-red">*</span></mat-label>                             \n'
                            param = param + '          <ckeditor [(ngModel)]="input.'+c_properties[index]+'" formControlName="'+c_properties[index]+'" [config]="{uiColor: \'#16c1c3\'}" \n'
                            param = param + '            [readonly]="false" debounce="500">                                                            \n'
                            param = param + '          </ckeditor>                                                                                     \n'

                        # check control is radio
                        if c_inputtypes[index] == 'radio':
                            param = param + '          <mat-label i18n>'+c_titles[index]+' <span class="text-red">*</span></mat-label>                           \n'
                            param = param + '          <mat-radio-group formControlName="'+c_properties[index]+'" [(ngModel)]="input.'+c_properties[index]+'" aria-label="'+c_titles[index]+'">          \n'
                            param = param + '            <mat-radio-button *ngFor="let sex of sexs" [value]="sex.value" style="padding-left: 10px;">   \n'
                            param = param + '              {{sex.viewValue}}                                                                           \n'
                            param = param + '            </mat-radio-button>                                                                           \n'
                            param = param + '          </mat-radio-group>                                                                              \n'

                        # check control is number
                        if c_inputtypes[index] == 'number':
                            param = param + '          <mat-form-field class="example-full-width">                                                     \n'
                            param = param + '            <mat-label i18n>'+c_titles[index]+' <span class="text-red">*</span></mat-label>                               \n'
                            param = param + '            <input matInput type="number" [(ngModel)]="input.'+c_properties[index]+'" formControlName="'+c_properties[index]+'">              \n'
                            param = param + '          </mat-form-field>                                                                               \n'

                        # check control is select
                        if c_inputtypes[index] == 'select':
                            refers = c_refers[index].split(':')
                            if len(refers) > 2:
                                refer_class = models.Class.objects.filter(id=refers[0])
                                refer_classname = refer_class[0].classname
                                refer_id = refers[1]
                                refer_display = refers[2]

                                param = param + '          <mat-form-field class="example-full-width">                                                     \n'
                                param = param + '            <mat-label i18n>'+c_titles[index]+'<span class="text-red">*</span></mat-label>                               \n'
                                param = param + '            <mat-select formControlName="'+c_properties[index]+'" [(ngModel)]="input.'+c_properties[index]+'">                                \n'
                                param = param + '              <mat-option *ngFor="let '+ refer_classname +' of '+ refer_classname +'Datas" [value]="'+ refer_classname +'.'+ refer_id +'">                           \n'
                                param = param + '                {{class.'+ refer_display +'}}                                                                            \n'
                                param = param + '              </mat-option>                                                                               \n'
                                param = param + '            </mat-select>                                                                                 \n'
                                param = param + '          </mat-form-field>                                                                               \n'

                        # checking validations
                        validates = c_validates[index].split(':')
                        if len(validates) > 0:
                            param = param + '                                                                                      \n'
                            param = param + '          <div class="alert alert-danger" *ngIf="form.controls[\''+c_properties[index]+'\'].invalid      \n'
                            param = param + '              && (form.controls[\''+c_properties[index]+'\'].dirty || form.controls[\''+c_properties[index]+'\'].touched)"> \n'

                            for validate in validates:
                                if validate == 'required':
                                    param = param + '            <div *ngIf="form.controls[\''+c_properties[index]+'\'].errors.required" i18n>                \n'
                                    param = param + '              Vui lòng nhập trường này.                                               \n'
                                    param = param + '            </div>                                                                    \n'

                                if validate == 'minLength':
                                    param = param + '            <div *ngIf="form.controls[\''+c_properties[index]+'\'].errors.minlength" i18n>               \n'
                                    param = param + '              Bạn vui lòng nhập ít nhất 1 ký tự.                                      \n'
                                    param = param + '            </div>                                                                    \n'

                                if validate == 'maxLength':
                                    param = param + '            <div *ngIf="form.controls[\''+c_properties[index]+'\'].errors.maxlength" i18n>               \n'
                                    param = param + '              Bạn không được nhập quá 100 ký tự.                                      \n'
                                    param = param + '            </div>                                                                    \n'

                                if validate == 'pattern':
                                    param = param + '            <div *ngIf="form.controls[\''+c_properties[index]+'\'].errors.pattern" i18n>                 \n'
                                    param = param + '              Vui lòng nhập đúng định dạng.                                           \n'
                                    param = param + '            </div>                                                                    \n'

                                if validate == 'min':
                                    param = param + '            <div *ngIf="form.controls[\''+c_properties[index]+'\'].errors.min" i18n>                     \n'
                                    param = param + '              Số không được nhỏ hơn 10.                                               \n'
                                    param = param + '            </div>                                                                    \n'

                                if validate == 'max':
                                    param = param + '            <div *ngIf="form.controls[\''+c_properties[index]+'\'].errors.max" i18n>                     \n'
                                    param = param + '              Số không được lớn hơn 100.                                              \n'
                                    param = param + '            </div>                                                                    \n'

                                if validate == 'email':
                                    param = param + '            <div *ngIf="form.controls[\''+c_properties[index]+'\'].errors.email" i18n>                   \n'
                                    param = param + '              Vui lòng nhập đúng định dạng email.                                     \n'
                                    param = param + '            </div>                                                                    \n'

                            param = param + '          </div>                                                                      \n'
                            param = param + '        </div>                                                                        \n\n'

                    params.append(param)
                    source_path_template = module_path_template + 'sample/sample-dialog.html'
                    dest_path_template = module_path + component_name + '/' + component_name + '-dialog.html'
                    core_gen.render_replace(source_path_template, dest_path_template, params)

                # html
                # load data crud for list
                crud = models.CRUD.objects.filter(idproject=idproject, idclass=table.id, actiontype=0)
                if len(crud) > 0:
                    crud = crud[0]
                    c_titles = crud.titles.split(',')
                    c_properties = crud.properties.split(',')
                    c_alias = crud.alias.split(',')
                    c_refers = crud.refers.split(',')
                    c_inputtypes = crud.inputtypes.split(',')
                    c_validates = crud.validates.split(',')
                    c_formats = crud.formats.split(',')

                    params = []
                    param = ''
                    params.append(classname)

                    # check have delete action
                    crud = models.CRUD.objects.filter(idproject=idproject, idclass=table.id, actiontype=3)
                    if len(crud) > 0:
                        param = '      <button type="button" class="btn btn-danger btn-del w-120" data-toggle="modal" data-target="#exampleModal" i18n><i \n'
                        param = param + '          class="mdi mdi-delete"></i>Xóa</button>                                                                        \n'
                        params.append(param)
                    else:
                        params.append('      <!--  -->')

                    # add column grid
                    param = ''
                    for index in range(len(c_properties)):
                        param = param + '    <!-- '+ c_properties[index] +' Column -->                                                    \n'
                        param = param + '    <ng-container matColumnDef="'+ c_properties[index] +'">                                      \n'

                        # check refer class
                        refers = c_refers[index].split(':')
                        if c_refers[index] != '' and refers[0] != '':
                            if len(refers) > 2:
                                refer_class = models.Class.objects.filter(id=refers[0])
                                refer_classname = refer_class[0].classname.capitalize()
                                refer_id = refers[1]
                                refer_display = refers[2]

                                # check alias
                                if c_alias[index] != '':
                                    param = param + '      <th mat-header-cell *matHeaderCellDef mat-sort-header i18n> ' + c_alias[index] + ' </th> \n'
                                else:
                                    param = param + '      <th mat-header-cell *matHeaderCellDef mat-sort-header i18n> ' + c_titles[index] + ' </th> \n'

                                # check format
                                param = param + '      <td mat-cell *matCellDef="let row"> {{getDisplay'+ refer_classname +'ById(row.'+ c_properties[index] +')}} </td>\n'

                        else:
                            # check alias
                            if c_alias[index] != '':
                                param = param + '      <th mat-header-cell *matHeaderCellDef mat-sort-header i18n> '+ c_alias[index] +' </th> \n'
                            else:
                                param = param + '      <th mat-header-cell *matHeaderCellDef mat-sort-header i18n> '+ c_titles[index] +' </th> \n'

                            # check format
                            if c_formats[index] != '':
                                param = param + '      <td mat-cell *matCellDef="let row"> {{'+ c_formats[index] +'}} </td>                \n'
                            else:
                                param = param + '      <td mat-cell *matCellDef="let row"> {{row.'+ c_properties[index] +'}} </td>                \n'

                        param = param + '    </ng-container>                                                         \n\n'

                    params.append(param)

                    source_path_template = module_path_template + 'sample/sample.component.html'
                    dest_path_template = module_path + component_name + '/' + component_name + '.component.html'
                    core_gen.render_replace(source_path_template, dest_path_template, params)

                # scss
                params = []
                source_path_template = module_path_template + 'sample/sample.component.scss'
                dest_path_template = module_path + component_name + '/' + component_name + '.component.scss'
                core_gen.render_replace(source_path_template, dest_path_template, params)

                # ts
                # load data crud for list
                crud = models.CRUD.objects.filter(idproject=idproject, idclass=table.id, actiontype=0)
                if len(crud) > 0:
                    crud = crud[0]
                    c_titles = crud.titles.split(',')
                    c_properties = crud.properties.split(',')
                    c_alias = crud.alias.split(',')
                    c_refers = crud.refers.split(',')
                    c_inputtypes = crud.inputtypes.split(',')
                    c_validates = crud.validates.split(',')
                    c_formats = crud.formats.split(',')

                    params = []
                    param = ''
                    # update @component and export class
                    param = param + '@Component({                                                                \n'
                    param = param + '  selector: \'app-c'+ str(ans + 1) +'-'+ classname +'\',                                                \n'
                    param = param + '  templateUrl: \'./c'+ str(ans + 1) +'-'+ classname +'.component.html\',                                \n'
                    param = param + '  styleUrls: [\'./c'+ str(ans + 1) +'-'+ classname +'.component.scss\'],                                \n'
                    param = param + '})                                                                          \n'
                    param = param + 'export class C'+ str(ans + 1) +''+ classname.capitalize() +'Component implements OnInit, AfterViewInit, OnDestroy {  \n'
                    params.append(param)
                    param = ''

                    # add display columns
                    for property in c_properties:
                        param = param + '    \''+ property +'\',\n'

                    params.append(param)
                    param = ''

                    # update what in getLengthOfPage method
                    params.append(str(ans))

                    # add data reference binding
                    param_define = ''
                    param_call = ''
                    param_method = ''
                    for c_refer in c_refers:
                        refers = c_refer.split(':')
                        if len(refers) > 0 and refers[0] != '':
                            refer_class = models.Class.objects.filter(id=refers[0])
                            refer_classname = refer_class[0].classname
                            refer_id = refers[1]
                            refer_display = refers[2]

                            param_define = param_define + '  '+ refer_classname +'Datas: any[] = [];\n'

                            param_call = param_call + '    // load list '+ refer_classname +'\n'
                            param_call = param_call + '    this.getList'+ refer_classname.capitalize() +'();\n\n'

                            param_method = param_method + '  /**                                                            \n'
                            param_method = param_method + '   * get list '+ refer_classname +'\n'
                            param_method = param_method + '   */                                                            \n'
                            param_method = param_method + '  getList'+ refer_classname.capitalize() +'() {       \n'

                            # get what number for select
                            all_class = models.Class.objects.filter(idproject=idproject)
                            count = 0
                            for index in range(len(all_class)):
                                if all_class[index].classname == refer_classname:
                                    count = index
                                    break

                            param_method = param_method + '    this.subscription.push(this.api.excuteAllByWhat({}, \''+ str(count+1) +'00\') \n'

                            param_method = param_method + '      .subscribe((data) => {                                     \n'
                            param_method = param_method + '        this.'+ refer_classname +'Datas = data;  \n'
                            param_method = param_method + '      })                                                         \n'
                            param_method = param_method + '    );                                                           \n'
                            param_method = param_method + '  }                                                              \n'
                            param_method = param_method + '                                                                 \n'
                            param_method = param_method + '  /**                                                            \n'
                            param_method = param_method + '   * get name display '+ refer_classname +' by id     \n'
                            param_method = param_method + '   */                                                            \n'
                            param_method = param_method + '  getDisplay'+ refer_classname.capitalize() +'ById(id) {                                      \n'
                            param_method = param_method + '    return this.'+ refer_classname +'Datas.filter((e) => e.id == id)[0]?.name;   \n'
                            param_method = param_method + '  }                                                              \n\n'

                    params.append(param_define)

                    # add for permission
                    params.append(chr(97 + ans))

                    params.append(param_call)
                    params.append(param_method)

                    # update what in onLoadDataGrid method
                    params.append(str(ans))

                    # update what in onBtnDelClick method
                    params.append(str(ans))

                    # update name dialog in onBtnInsertDataClick method
                    params.append('C'+ str(ans + 1) +''+ classname.capitalize() +'Dialog')

                    # update name dialog in onBtnUpdateDataClick method
                    params.append('C' + str(ans + 1) + '' + classname.capitalize() + 'Dialog')

                    param = ''

                    # start for dialog component
                    # update @component and export dialog class
                    param = param + '@Component({                                              \n'
                    param = param + '  selector: \'c'+ str(ans + 1) +'-'+ classname +'-dialog\',                            \n'
                    param = param + '  templateUrl: \'c'+ str(ans + 1) +'-'+ classname +'-dialog.html\',                    \n'
                    param = param + '  styleUrls: [\'./c'+ str(ans + 1) +'-'+ classname +'.component.scss\'],               \n'
                    param = param + '})                                                        \n'
                    param = param + 'export class C'+ str(ans + 1) + classname.capitalize() +'Dialog implements OnInit, OnDestroy {  \n'

                    params.append(param)
                    param = ''

                    # get list for insert
                    crud = models.CRUD.objects.filter(idproject=idproject, idclass=table.id, actiontype=1)
                    if len(crud) > 0:
                        crud = crud[0]
                        c_properties = crud.properties.split(',')
                        c_validates = crud.validates.split(',')

                    # add input value for dialog insert
                    for property in c_properties:
                        param = param + '    '+ property +': \'\',\n'

                    params.append(param)
                    param = ''

                    # add data reference binding for dialog
                    param_define = ''
                    param_call = ''
                    param_method = ''
                    for c_refer in c_refers:
                        refers = c_refer.split(':')
                        if len(refers) > 0 and refers[0] != '':
                            refer_class = models.Class.objects.filter(id=refers[0])
                            refer_classname = refer_class[0].classname
                            refer_id = refers[1]
                            refer_display = refers[2]

                            param_define = param_define + '  ' + refer_classname + 'Datas: any[] = [];\n'

                            param_call = param_call + '    // load list ' + refer_classname + '\n'
                            param_call = param_call + '    this.getList' + refer_classname.capitalize() + '();\n\n'

                            param_method = param_method + '  /**                                                            \n'
                            param_method = param_method + '   * get list ' + refer_classname + '\n'
                            param_method = param_method + '   */                                                            \n'
                            param_method = param_method + '  getList' + refer_classname.capitalize() + '() {       \n'

                            # get what number for select
                            all_class = models.Class.objects.filter(idproject=idproject)
                            count = 0
                            for index in range(len(all_class)):
                                if all_class[index].classname == refer_classname:
                                    count = index
                                    break

                            param_method = param_method + '    this.subscription.push(this.api.excuteAllByWhat({}, \'' + str(count + 1) + '00\') \n'

                            param_method = param_method + '      .subscribe((data) => {                                     \n'
                            param_method = param_method + '        this.' + refer_classname + 'Datas = data;  \n'
                            param_method = param_method + '      })                                                         \n'
                            param_method = param_method + '    );                                                           \n'
                            param_method = param_method + '  }                                                              \n\n'

                    params.append(param_define)

                    # update name dialog in constructor method
                    params.append('C' + str(ans + 1) + '' + classname.capitalize() + 'Dialog')

                    # add define validate
                    param = ''

                    for index in range(len(c_properties)):
                        param = param + '      '+ c_properties[index] +': [                        \n'
                        param = param + '        null,                        \n'
                        param = param + '        [                            \n'
                        validates = c_validates[index].split(':')
                        for validate in validates:
                            if validate == 'required':
                                param = param + '          Validators.required,       \n'

                            if validate == 'minLength':
                                param = param + '          Validators.minLength(1),   \n'

                            if validate == 'maxLength':
                                param = param + '          Validators.maxLength(100), \n'

                            if validate == 'pattern':
                                param = param + '          Validators.pattern(\' * \'),   \n'

                            if validate == 'min':
                                param = param + '          Validators.min(10),        \n'

                            if validate == 'max':
                                param = param + '          Validators.max(100),       \n'

                            if validate == 'email':
                                param = param + '          Validators.email,          \n'
                        param = param + '        ],                           \n'
                        param = param + '      ],                             \n'

                    params.append(param)

                    params.append(param_call)
                    params.append(param_method)

                    # add for mat date for field datetime
                    # get list for insert
                    crud = models.CRUD.objects.filter(idproject=idproject, idclass=table.id, actiontype=1)
                    if len(crud) > 0:
                        crud = crud[0]
                        c_properties = crud.properties.split(',')
                        c_inputtypes = crud.inputtypes.split(',')

                    format_date = ''
                    for index in range(len(c_properties)):
                        if c_inputtypes[index] == 'date' or c_inputtypes[index] == 'datetime':
                            format_date = format_date + '    this.input.'+ c_properties[index] +' = this.api.formatDate(new Date(this.input.'+ c_properties[index] +')); \n'

                    params.append(format_date)

                    # update what in onBtnSubmitClick method
                    params.append(str(ans))

                    source_path_template = module_path_template + 'sample/sample.component.ts'
                    dest_path_template = module_path + component_name + '/' + component_name + '.component.ts'
                    core_gen.render_replace(source_path_template, dest_path_template, params)

                # module
                # load data crud for list
                params = []
                param = ''
                class_component = 'C'+ str(ans + 1) +''+ classname.capitalize() +'Component'
                class_dialog = 'C'+ str(ans + 1) +''+ classname.capitalize() +'Dialog'
                component_link = './c'+ str(ans + 1) +'-'+ classname +'.component'
                class_module = 'C'+ str(ans + 1) +''+ classname.capitalize() +'Module'

                # import dialog and component
                param = param + 'import { '+ class_component +', '+ class_dialog +' } from \'./'+ component_link +'\';  \n'
                params.append(param)

                # add component to import
                # import dialog and component
                param = ''
                param = param + '  declarations: ['+ class_component +', '+ class_dialog +'],   \n'
                params.append(param)
                params.append(class_component)
                params.append(class_dialog)
                params.append(class_module)

                source_path_template = module_path_template + 'sample/sample.module.ts'
                dest_path_template = module_path + component_name + '/' + component_name + '.module.ts'
                core_gen.render_replace(source_path_template, dest_path_template, params)

                # update permission
                roles = roles + ',' + chr(97 + ans) + ':1'

                permission = permission + '    {                          \n'
                permission = permission + '      value: \''+ chr(97+ans) +'\',            \n'
                permission = permission + '      viewValue: \'Quản lý '+ classname.capitalize() +' \', \n'
                permission = permission + '    },                         \n'

                ans = ans + 1
    
            # render replace
            # c1-account
            source_path_template = 'frontend/angular/src/app/home-page/content/c1-account/c1-account.component.ts'
            dest_path_template = project_name + '/frontend/src/app/home-page/content/c1-account/c1-account.component.ts'
            core_gen.render_replace(source_path_template, dest_path_template, [roles, permission])

            # menu html
            source_path_template = 'frontend/angular/src/app/home-page/menu/menu.component.html'
            dest_path_template = project_name + '/frontend/src/app/home-page/menu/menu.component.html'
            core_gen.render_replace(source_path_template, dest_path_template, [html_menu])

            # menu component
            source_path_template = 'frontend/angular/src/app/home-page/menu/menu.component.ts'
            dest_path_template = project_name + '/frontend/src/app/home-page/menu/menu.component.ts'
            core_gen.render_replace(source_path_template, dest_path_template, [param_permision_menu, load_permision_menu])

            # content module
            source_path_template = 'frontend/angular/src/app/home-page/content/content.module.ts'
            dest_path_template = project_name + '/frontend/src/app/home-page/content/content.module.ts'
            core_gen.render_replace(source_path_template, dest_path_template, [content_module])

        else:
            print('project havent class')

