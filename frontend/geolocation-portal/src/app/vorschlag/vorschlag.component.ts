import { Component, OnInit, ViewChild } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { Category } from '../category';
import { CategoryService } from '../category.service';
import { ModalDirective } from "node_modules/angular-bootstrap-md/lib/free/modals/modal.directive";

@Component({
  selector: 'app-vorschlag',
  templateUrl: './vorschlag.component.html',
  styleUrls: ['./vorschlag.component.css']
})
export class VorschlagComponent implements OnInit {
  submissionForm: FormGroup;
  categories: Category []= [];
  formInvalid: boolean = false;
  @ViewChild('frameModal', {static: false}) modalDirective: ModalDirective;


  constructor(private categoryService: CategoryService) { }

  ngOnInit() {

    this.getCategories();

    this.submissionForm = new FormGroup({
      contactFormName: new FormControl('', [<any>Validators.required]),
      contactFormLastName: new FormControl('', [<any>Validators.required]),
      contactFormEmail: new FormControl('', [<any>Validators.required, <any>Validators.email]),
      contactFormSubjects: new FormControl('', [<any>Validators.required]),
      contactFormMessage: new FormControl('', [<any>Validators.required]),
    });


  }


  getCategories(){
    this.categoryService.getCategoriesFromAPI().subscribe(categories => (this.categories = categories));
  }
 


  get contactFormEmail() {
    return this.submissionForm.get('contactFormEmail');
  }
  get contactFormName() {
    return this.submissionForm.get('contactFormName');
  }
  get contactFormLastName() {
    return this.submissionForm.get('contactFormLastName');
  }
  get contactFormSubjects() {
    return this.submissionForm.get('contactFormSubjects');
  }
  get contactFormMessage() {
    return this.submissionForm.get('contactFormMessage');
  }

  onSubmit(){
   if(this.submissionForm.valid){
    this.modalDirective.show();
    this.submissionForm.reset();
    this.formInvalid = false;

   }
   else{
    this.formInvalid= true;
   }
  }





  /* alte Funktion ohne API 
  getCategories(){
    this.categoryService.getCategories().subscribe(Category => (this.categories = Category));
  } */
}
