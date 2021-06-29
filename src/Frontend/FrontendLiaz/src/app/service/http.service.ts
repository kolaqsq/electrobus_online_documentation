import {Injectable} from "@angular/core";
import {HttpClient} from "@angular/common/http";
import {Observable, pipe} from "rxjs";

@Injectable({providedIn: 'root'})
export class HttpService{

  constructor(private http: HttpClient) {
  }

  public option(url: string): Observable<any>{
    return this.http.options(url);
  }

  public get(url: string): Observable<any>{
    return this.http.get(url);
  }
}
