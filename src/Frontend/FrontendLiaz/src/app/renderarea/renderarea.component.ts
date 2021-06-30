import {Component, Injectable, OnInit} from "@angular/core";
import {HttpService} from "../service/http.service";
import {Location} from '@angular/common';

@Component({
  selector: 'app-renderarea',
  templateUrl: './renderarea.component.html',
  styleUrls: ['./renderarea.component.scss']
})

@Injectable({providedIn: 'root'})

export class RenderareaComponent implements OnInit {

  constructor(private HttpService: HttpService, private location: Location) {
  }

  url =  "http://liaz-demo.std-950.ist.mospolytech.ru"
  request = {}
  isActive = 'main'
  header = ''
  search = ''

  ngOnInit(): void {
    this.GetRequest(this.url)
    this.recentPage(window.location.href)
  }

  recentPage(url:string){
    if (url.split('/').length == 3){
      this.isClicked(this.url, 'main', '')
    }
    if (url.split('/').length == 4 && url.split('/')[3] != ""){
      let res:string = url.split('/')[3]
      this.isClicked(this.url + '/' + res, 'next', res)
    }
    if (url.split('/').length == 5){
      let res:string = url.split('/')[3] + '/' + url.split('/')[4]
      this.isClicked(this.url + '/' + res, 'detail', res)
    }
  }

  GetRequest(added_path?: string){
    if (added_path != undefined){
      this.HttpService.get(added_path).subscribe(value => {
        this.request = value
        console.log(value)
      }, err => {
        console.error(err)
      })
    }
  }

  isClicked(url: string, state: string, header?: string){
    switch (state){
      case "main": {
        this.isActive = "main"
        this.GetRequest(url)
        this.location.replaceState("")
        break
      }
      case "next": {
        this.isActive = "con"
        this.GetRequest(url)
        this.location.replaceState(header)
        break
      }
      case "detail": {
        this.isActive = "detail"
        this.GetRequest(url)
        this.location.replaceState(header)
        break
      }
    }
  }
}
