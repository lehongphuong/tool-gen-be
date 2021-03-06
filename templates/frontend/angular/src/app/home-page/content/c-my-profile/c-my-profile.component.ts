import { Component, OnInit, OnDestroy } from '@angular/core';
import { ApiService } from '../../../common/api-service/api.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { MustMatch } from 'src/app/common/validations/must-match.validator';
import { Md5 } from 'ts-md5';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-i-my-profile',
  templateUrl: './c-my-profile.component.html',
  styleUrls: ['./c-my-profile.component.scss'],
})
export class CMyProfileComponent implements OnInit, OnDestroy {

  //data binding
  staff = {
    id: '',
    email: '',
    phone: '',
    address: '',
    name: '',
    password: '',
    img: '',
    created_date: '',
  };

  staffInfoLogin = {
    id: '',
    email: '',
    phone: '',
    address: '',
    name: '',
    password: '',
    img: '',
    created_date: '',
  };

  //value hide
  hide = true;
  hide1 = true;
  hide2 = true;

  //password
  passwordMdOld: any;
  passwordMdNew: any;

  //old password
  oldpassword: string;

  //new password
  newpassword: string;

  //repassword
  repassword: string;

  // validate
  form: FormGroup;

  formresetpass: FormGroup;

  /** for table */
  subscription: Subscription[] = [];

  // flag insert
  insertFlag: boolean = false;

  /**
   * constructor
   * @param api
   * @param formBuilder
   */
  constructor(private api: ApiService, private formBuilder: FormBuilder) {
    // add validate for controls
    this.form = this.formBuilder.group({
      name: [null, [Validators.required, Validators.minLength(5), Validators.maxLength(50)]],
      email: [null],
      phone: [null],
      address: [null],
    });

    //form validation
    this.formresetpass = this.formBuilder.group({
      password: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(50)]],
      newpassword: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(50),],],
      repassword: [null, [Validators.required, Validators.minLength(8), Validators.maxLength(50),],],
    }, 
      //check newPassword == rePassword
      { validator: MustMatch('newpassword', 'repassword') }
    );
  }

  /**
   * ngOnInit
   */
  ngOnInit(): void {
    // on Close Sidebar Mobile
    this.onCloseSidebarMobile();

    // get staff value
    this.staff = this.api.accountSubject.value;

    // getDataStaffLogin
    this.getDataStaffLogin();

    //scroll top mobile
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
   * get Data Staff Login
   */
  getDataStaffLogin() {
    const param = {
      id: this.staff['id']
    };

    // get data staff login
    this.subscription.push(this.api.excuteAllByWhat(param, '6').subscribe((data) => {
      if (data) {
        // set logo default
        if (data[0]['img'] == '' || data[0]['img'] == undefined) {
          data[0]['img'] = "../../../assets/images/logo-admin.png"
        }

        this.staffInfoLogin = data[0];
      }
    })
    );
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
   * on update info staff
   */
  onBtnUpdateClick() {
    const param = {
      id: this.staffInfoLogin['id'],
      name: this.staffInfoLogin['name'],
    };

    //update profile
    this.subscription.push(this.api.excuteAllByWhat(this.staffInfoLogin, '2').subscribe((data) => {
      if (data) {
        this.api.showSuccess('Cập nhật thành công ');
      }
    })
    );
  }

  /**
   * on update img
   */
  onBtnUploadImgClick() {
    const param = {
      id: this.staffInfoLogin['id'],
      img: this.staffInfoLogin['img'],
    };

    //check validation
    if (this.form.status != 'VALID') {
      this.api.showWarning('Vui lòng nhập các mục đánh dấu * ');
      return;
    } else {

      //update img in profile
      this.subscription.push(this.api.excuteAllByWhat(param, '9').subscribe((data) => {
        if (data) {
          this.api.showSuccess('Cập nhật thành công ');
        }
      })
      );
    }
  }

  /**
   * on Change Password
   */
  onChangePassClick() {
    // return if error
    if (this.formresetpass.status != 'VALID') {
      this.api.showWarning('Vui lòng nhập các mục đánh dấu *');
      return;
    }

    //encode password
    this.passwordMdNew = Md5.hashAsciiStr(this.newpassword).toString();
    this.passwordMdOld = Md5.hashAsciiStr(this.oldpassword).toString();
    this.oldpassword = this.passwordMdOld;

    const param = {
      password: this.passwordMdNew,
      id: this.staff.id,
    };

    //if password enter = password login
    if (this.oldpassword == this.staffInfoLogin['password']) {
      // this.staff.password = this.newpassword;

      //update password
      this.subscription.push(this.api.excuteAllByWhat(param, '7').subscribe((data) => {
        if (data) {
          this.api.showSuccess('Cập nhật mật khẩu thành công ');
          this.formresetpass.reset();

          // load data staff to get password new
          this.getDataStaffLogin();
        }
      })
      );
    } else {
      this.api.showWarning('Mật khẩu cũ chưa đúng hoặc mật khẩu mới chưa trùng nhau ');
      this.formresetpass.reset();
    }
  }

  /**
   * on button Cancel
   */
  onBtnCancelClick() {
    this.formresetpass.reset();
  }
}
