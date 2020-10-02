import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ContentComponent } from './content.component';
import { RouterModule } from '@angular/router';
import { TransferHttpCacheModule } from '@nguniversal/common';
import { ApiService } from '../../common/api-service/api.service';
import { IMyProfileModule } from './c-my-profile/c-my-profile.module';

@NgModule({
  declarations: [ContentComponent],
  imports: [
    TransferHttpCacheModule,
    CommonModule,
    RouterModule.forChild([
      {
        // ng g module home-page/content/sellTicket --module content
        // ng g c home-page/content/sellTicket
        path: '',
        component: ContentComponent,
        children: [
          {
            path: 'my-profile',
            loadChildren: () =>
              import('./c-my-profile/c-my-profile.module').then(
                (m) => m.IMyProfileModule
              ),
          },
          {
            path: 'home',
            loadChildren: () =>
              import('./c0-home/home.module').then((m) => m.HomeModule),
          },
          {
            path: 'c1-account',
            loadChildren: () =>
              import('./c1-account/c1-account.module').then((m) => m.C1AccountModule),
          },

phuong0

        ],
      },
    ]),
    IMyProfileModule,
  ],
  providers: [ApiService],
  entryComponents: [],
})
export class ContentModule { }
