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

    $(function () {
      
     var mybutton = document.getElementById("back-to-top");

      // When the user scrolls down 20px from the top of the document, show the button
      $(window).on('scroll', scrollFunction());

      function scrollFunction() {
        console.log(document.body.scrollTop);
        if (document.body.scrollTop > 30|| document.documentElement.scrollTop > 30) {
          mybutton.style.display = "block";;
        } else {
          mybutton.style.display = "none";
        }
      }
  
    });
  }


  scrollToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }
}
