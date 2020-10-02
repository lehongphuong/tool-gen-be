import { Component, OnInit } from '@angular/core';
import { LoginCookie } from '../../common/core/login-cookie';
import { ApiService } from 'src/app/common/api-service/api.service';
// import $ from 'jquery';
import * as $ from 'jquery';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss'],
})
export class MenuComponent implements OnInit {
  //menu flag
  menuFlag: boolean = false;
  menuMobileFlag: boolean = false;
  menuMobileStaff: boolean = false;
  settingButton: boolean = false;
  searchFlag: boolean = false;
  isMobile: boolean = false;
  idStaff: Number;

  // flag for menu
  navLeft: boolean = false;
  navLeftMobile: boolean = false;
  settingFlag: boolean = false;

  //data permission menu
  isPermissionMenu1: boolean = false;
phuong0

  // show dropdown (logout/myprofile/changepasswork)
  isShow: boolean = false;
  info: any = null;

  //pubic is visited
  public isVisited = false;
  public checkVisited() {
    // reverse the value of property
    this.isVisited = !this.isVisited;
  }

  //data binding
  staff: any;

  staffInfoLogin = {
    id: '',
    email: '',
    name: '',
    passwork: '',
    img: '',
    created_date: '',
  };

  subscription: Subscription[] = [];

  /**
   * constructor
   * @param login
   * @param api
   */
  constructor(private login: LoginCookie, public api: ApiService) {
    // get staff value
    this.staff = this.api.getAccountValue;
  }

  /**
   * ngOnInit
   */
  ngOnInit() {
    this.staff = this.api.accountSubject.value;
    this.idStaff = this.api.accountSubject.value.id;
    this.isMobile = this.isMobileDevice();
    this.onLoadPermission();

    // toggle Sidebar Click
    this.toggleSidebarClick();

    // toggle Sidebar Mobile Click
    this.toggleSidebarMobileClick();

    // getDataStaffLogin
    this.getDataStaffLogin();
  }

  /**
     * ngAfterViewInit
     */
  ngAfterViewInit() {
    // process click of menu response
    $(document).ready(
      function ($) {
        'use strict';
        //Open submenu on hover in compact sidebar mode and horizontal menu mode
        $(document).on('mouseenter mouseleave', '.sidebar .nav-item', function (ev) {
          var body = $('#body');
          var sidebarIconOnly = body.hasClass("sidebar-icon-only");
          var horizontalMenu = body.hasClass("horizontal-menu");
          var sidebarFixed = body.hasClass("sidebar-fixed");
          if (!('ontouchstart' in document.documentElement)) {
            if (sidebarIconOnly || horizontalMenu) {
              if (sidebarFixed) {
                if (ev.type === 'mouseenter') {
                  body.removeClass('sidebar-icon-only');
                }
              }
              else {
                var $menuItem = $(this);
                if (ev.type === 'mouseenter') {
                  $menuItem.addClass('hover-open')
                }
                else {
                  $menuItem.removeClass('hover-open')
                }
              }
            }
          }
        });
      }
    );
  }

  /**
   * ngOnDestroy
   */
  ngOnDestroy(): void {
    throw new Error("Method not implemented.");
  }

  /**
   * get Data Staff Login
   */
  getDataStaffLogin() {
    const param = {
      id: this.staff.id
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
   * onLoadPermission
   */
  onLoadPermission() {
    // load permission
    if (this.staff.role.search('a:1') < 0) {
      this.isPermissionMenu1 = true;
    }

phuong1
  }

  /**
   * is Mobile Device
   */
  isMobileDevice() {
    return (
      typeof window.orientation !== 'undefined' ||
      navigator.userAgent.indexOf('IEMobile') !== -1
    );
  }

  /**
   * onBtnLogOutStaffClick
   */
  onBtnLogOutStaffClick() {
    this.api.logoutAccount();
  }

  /**
   * logOut Staff
   */
  toggleSidebarClick() {
    $(document).ready(function () {
      $(".icon-toggle-sidebar").click(function () {
        $("html body").toggleClass("sidebar-icon-only");
      });
    });
  }

  /**
   * logOut Staff
   */
  toggleSidebarMobileClick() {
    $(document).ready(function () {
      $(".navbar-toggler-right").click(function () {
        $(".row-offcanvas-right").toggleClass("active");
      });
    });
  }

  /**
     * onToggleButtonDesktopClick
     */
  onToggleButtonDesktopClick() {
    this.navLeft = !this.navLeft;
  }

  /**
   * onToggleButtonMobileClick
   */
  onToggleButtonMobileClick() {
    this.navLeftMobile = !this.navLeftMobile;
  }

  onSettingButtonClick() {
    this.settingFlag = !this.settingFlag;
  }

}
