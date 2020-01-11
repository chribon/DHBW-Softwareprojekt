import { Component, OnInit } from '@angular/core';
import * as $ from 'jquery';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  constructor() { }

  ngOnInit() {

  }


  scrollToTop():void {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
  displayChatBot():void{

  }

}
