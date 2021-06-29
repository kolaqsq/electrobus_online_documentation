import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { RenderareaComponent } from './renderarea/renderarea.component';
import {ContentComponent} from "./content/content.component";
import {HttpClientModule} from "@angular/common/http";
import {renderareaPipe} from "./renderarea/renderarea.pipe";
import {FormsModule} from "@angular/forms";

@NgModule({
  declarations: [
    AppComponent,
    RenderareaComponent,
    ContentComponent,
    renderareaPipe
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
