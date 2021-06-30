import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter'
})

export class renderareaPipe implements PipeTransform {

  transform(value: any, searchValue): any {
    console.log(value)
  }

}
