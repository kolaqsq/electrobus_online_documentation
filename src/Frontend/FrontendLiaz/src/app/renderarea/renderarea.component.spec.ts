import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RenderareaComponent } from './renderarea.component';

describe('RenderareaComponent', () => {
  let component: RenderareaComponent;
  let fixture: ComponentFixture<RenderareaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RenderareaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RenderareaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
