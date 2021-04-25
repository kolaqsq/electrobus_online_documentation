import { Component, OnInit } from '@angular/core';
import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class SimpleService {
  public count$ = new Subject<string>();

  public changeCount(count: string) {
    this.count$.next(count);
  }
}

export interface Text{
  id: number
  title: string
  text: string
}

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrls: ['./content.component.scss']
})
export class ContentComponent implements OnInit {
  public isActive = [true, true, true, true, true]
  public isFocused = 0
  public texts: Text[] = [
    {id: 1, title: 'Глава 1', text: 'Текст по главе 1'},
    {id: 2, title: 'Раздел 1', text: 'Текст по разделу 1'},
    {id: 3, title: 'Раздел 2', text: 'Текст по разделу 2'},
    {id: 4, title: 'Подраздел 1', text: 'Текст по подразделу 1'},
  ]
  public text = ['ff', 'dd']

  ngOnInit(): void {
  }

  public ReverseActive(id) {
    (this.isActive)[id] = !(this.isActive)[id]
  }

  public ChangedFocus(id){
    (this.isFocused) = id
  }

}
