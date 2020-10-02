import { Component, OnInit, Inject, ViewChild, OnDestroy } from '@angular/core';
import { ApiService } from '../../../common/api-service/api.service';
import { MatDialog, MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';
import { MatTableDataSource } from '@angular/material/table';
import { MatPaginator } from '@angular/material/paginator';
import { MatSort } from '@angular/material/sort';
import { Observable, Observer, Subscription } from 'rxjs';
import { SelectionModel } from '@angular/cdk/collections';
import { FormGroup, FormBuilder, Validators, FormControl, } from '@angular/forms';
import * as moment from 'moment';

@Component({
  selector: 'app-c1-account',
  templateUrl: './c1-account.component.html',
  styleUrls: ['./c1-account.component.scss'],
})
export class C1AccountComponent implements OnInit, OnDestroy {
  // subscription
  subscription: Subscription[] = [];

  /** for table */
  displayedColumns: string[] = ['select', 'name', 'email', 'created_date', 'edit',];

  dataSource: MatTableDataSource<any>;

  @ViewChild(MatPaginator, { static: false }) paginator: MatPaginator;
  @ViewChild(MatSort, { static: false }) sort: MatSort;

  applyFilter(filterValue: string) {
    this.dataSource.filter = filterValue.trim().toLowerCase();

    if (this.dataSource.paginator) {
      this.dataSource.paginator.firstPage();
    }
  }

  selection = new SelectionModel<any>(true, []);

  // update pagination
  pageIndex = 0;
  pageLength = 0;
  pageSize = 10;
  pageSizeOptions: number[] = [10, 20, 50, 100];

  /**
   * getLengthOfPage
   */
  getLengthOfPage() {
    this.subscription.push(
      this.api.excuteAllByWhat({}, '11').subscribe((data) => {
        if (data) {
          this.pageLength = data[0]['COUNT(1)'];
        } else {
          this.pageLength = 0;
        }
      })
    );
  }

  /**
   * onPageChange
   */
  onPageChange(event) {
    this.pageSize = event.pageSize;
    this.pageIndex = event.pageIndex;

    this.loadDataAccount();
  }

  /** Whether the number of selected elements matches the total number of rows. */
  isAllSelected() {
    if (this.dataSource) {
      const numSelected = this.selection.selected.length;
      const numRows = this.dataSource.data.length;
      return numSelected === numRows;
    }
    return null;
  }

  /** Selects all rows if they are not all selected; otherwise clear selection. */
  masterToggle() {
    this.isAllSelected()
      ? this.selection.clear()
      : this.dataSource.data.forEach((row) => this.selection.select(row));
  }

  /** The label for the checkbox on the passed row */
  checkboxLabel(row?: any): string {
    if (!row) {
      return `${this.isAllSelected() ? 'select' : 'deselect'} all`;
    }
    return `${this.selection.isSelected(row) ? 'deselect' : 'select'} row ${
      row.position + 1
      }`;
  }
  /** end for table */

  // data binding value
  input = {
    name: '',
    email: '',
    password: '',
    created_date: '',
    role: '',
  };

  // is permission menu
  havePermissionMenuC1: boolean = false;

  // acoount list
  accounts: any[];

  // role
  account = {
    email: '',
    role: '',
  };

  /**
   * constructor
   * @param api
   * @param dialog
   */
  constructor(private api: ApiService, public dialog: MatDialog) {
  }

  /**
   * ngOnInit
   */
  ngOnInit() {
    // load data account
    this.loadDataAccount();

    // get account login
    this.account = this.api.accountSubject.value;

    this.onLoadMenuPermission();

    // on Close Sidebar Mobile
    this.onCloseSidebarMobile();

    // scroll top mobile
    window.scroll({ left: 0, top: 0, behavior: 'smooth' });
  }

  /**
   * ngOnDestroy
   */
  ngOnDestroy() {
    this.subscription.forEach((item) => {
      item.unsubscribe();
    });
  }

  /**
   * on Close Sidebar Mobile
   */
  onCloseSidebarMobile() {
    $(document).ready(function () {
      $(".row-offcanvas-right").removeClass("active");
    });
  }

  /**
   * on Load menu Permission
   */
  onLoadMenuPermission() {
    // load permission
    if (this.account.role.search('a:3') >= 0) {
      this.havePermissionMenuC1 = true;
    }
  }

  /**
   * load data account
   */
  loadDataAccount() {
    // get Length Of Page
    this.getLengthOfPage();

    const param = { 'offset': Number(this.pageIndex * this.pageSize), 'limit': this.pageSize };
    //select all data account
    this.subscription.push(
      this.api.excuteAllByWhat(param, '10').subscribe((data) => {
        if (data) {
          // set data for table
          this.accounts = data;
          this.dataSource = new MatTableDataSource(data);
        } else {
          this.dataSource = new MatTableDataSource([]);
        }

        this.dataSource.sort = this.sort;
        this.selection = new SelectionModel<any>(true, []);
      })
    );
  }

  /**
   * on Delete Click
   */
  onBtnDelClick() {
    // get listId selection example: listId='1,2,6'
    let listId = '';
    this.selection.selected.forEach((item) => {
      if (listId == '') {
        listId += item.id;
      } else {
        listId += ',' + item.id;
      }
    });

    const param = { listid: listId };

    // start delete
    if (listId !== '') {
      // delete account id
      this.subscription.push(
        this.api.excuteAllByWhat(param, '3').subscribe((data) => {
          // load data account
          this.loadDataAccount();

          //scroll top
          window.scroll({ left: 0, top: 0, behavior: 'smooth' });

          // show toast success
          this.api.showSuccess('Xóa thành công ');
        })
      );
    } else {
      // show toast warning
      this.api.showWarning('Vui lòng chọn 1 mục để xóa ');
    }
    this.selection = new SelectionModel<any>(true, []);
  }

  /**
   * on insert data
   * @param event
   */
  onBtnInsertDataClick() {
    const dialogRef = this.dialog.open(C1AccountDialog, {
      width: '700px',
      data: { type: 0 },
      panelClass: 'custom-dialog',
    });

    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.loadDataAccount();
      }
    });

  }

  /**
   * on update data
   * @param event
   */
  onBtnUpdateDataClick(row) {
    const dialogRef = this.dialog.open(C1AccountDialog, {
      width: '700px',
      data: { type: 1, input: row },
      panelClass: 'custom-dialog',
    });

    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.loadDataAccount();
      }
    });
  }
}

/**
 * Component show thông tin để insert hoặc update
 */
@Component({
  selector: 'app-c1-account',
  templateUrl: 'c1-account-dialog.component.html',
  styleUrls: ['./c1-account.component.scss'],
})
export class C1AccountDialog implements OnInit, OnDestroy {
  observable: Observable<any>;
  observer: Observer<any>;
  type: number = 0;

  //subscription
  subscription: Subscription[] = [];

  // init input value
  input = {
    id: '',
    name: '',
    email: '',
    password: null,
    phone: '',
    address: '',
    created_date: new Date(),
    role: 'a:1phuong0',
    img: ''
  };

  date = new FormControl(moment());

  // sex value
  sexs: any[] = [
    { value: '1', viewValue: 'Nam' },
    { value: '0', viewValue: 'Nữ' },
  ];

  // list Permission
  listComponents = [
    {
      value: 'a',
      viewValue: 'Quản trị Nhân Viên',
    },
phuong1
  ];

  // options permission
  options = [
    {
      value: '1',
      viewValue: 'Không',
    },
    {
      value: '2',
      viewValue: 'Chỉ xem',
    },
    {
      value: '3',
      viewValue: 'Quản trị',
    },
  ];

  // list permission in array
  permissions: any[] = [];

  // form
  form: FormGroup;

  // detail user
  detailUser: any;

  /**
   * constructor
   * @param dialogRef
   * @param data
   * @param api
   * @param formBuilder
   */
  constructor(
    public dialogRef: MatDialogRef<C1AccountDialog>,
    @Inject(MAT_DIALOG_DATA) public data: any,
    private api: ApiService,
    private formBuilder: FormBuilder
  ) {
    this.type = data.type;

    console.log('data input1', this.input);

    // if type == 1 -> update
    if (this.type == 1) {
      this.input = data.input;
      console.log('data input', this.input);
    }

    // add validate for controls
    this.form = this.formBuilder.group({
      name: [
        null,
        [
          Validators.required,
          Validators.minLength(5),
          Validators.maxLength(100),
        ],
      ],
      email: [
        null,
        [
          Validators.required,
          Validators.minLength(5),
          Validators.maxLength(255),
          Validators.email,
        ],
      ],
      created_date: [null, [Validators.required]],
    });

    // xử lý bất đồng bộ
    this.observable = Observable.create((observer: any) => {
      this.observer = observer;
    });
  }

  /**
   * ngOnInit
   */
  ngOnInit() {
    // insert 
    if (this.type == 0) {
      let listPermissionsAr = this.input.role.split(',');
      listPermissionsAr.forEach((element) => {
        let subPerAr = element.split(':');
        this.permissions.push({ component: subPerAr[0], option: subPerAr[1] });
      });
    } else {
      this.getDataAccountById();
    }
  }

  /**
   * ngOnDestroy
   */
  ngOnDestroy() {
    this.subscription.forEach((item) => {
      item.unsubscribe();
    });
  }

  /**
   * get account by id
   */
  getDataAccountById() {
    const param = { id: this.input.id };

    //select all data account where id
    this.subscription.push(this.api.excuteAllByWhat(param, '6').subscribe((data) => {
      if (data.length > 0) {
        this.detailUser = data[0];
      }

      this.processedListPermission();
    })
    );
  }

  /**
   * processed List Permission to array
   */
  processedListPermission() {
    let listPermissionsAr = this.detailUser.role.split(',');
    listPermissionsAr.forEach((element) => {
      let subPerAr = element.split(':');
      this.permissions.push({ component: subPerAr[0], option: subPerAr[1] });
    });
  }

  /**
   * on Button Update Click
   */
  onBtnUpdateClick(): void {
    let listPermissionsStr = '';

    //handling update permission
    this.permissions.forEach((element) => {
      if (listPermissionsStr == '') {
        listPermissionsStr += element.component + ':' + element.option;
      } else {
        listPermissionsStr += ',' + element.component + ':' + element.option;
      }
    });

    //assign role = handling update permission
    this.input.role = listPermissionsStr;

    // update account
    this.subscription.push(
      this.api.excuteAllByWhat(this.input, (1 + this.type) + '').subscribe((data) => {
        this.dialogRef.close(true);
        this.api.showSuccess('Xử lý thành công ');
      })
    );
  }
}
