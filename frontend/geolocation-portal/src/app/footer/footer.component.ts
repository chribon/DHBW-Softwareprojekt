import { Component, OnInit, Renderer2, Inject, ViewChild } from '@angular/core';
import { DOCUMENT } from '@angular/common';
import { ModalDirective } from 'angular-bootstrap-md';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {
  
  @ViewChild('cookieModal', {static: false}) modalDirective: ModalDirective;

  constructor(private renderer2: Renderer2, @Inject(DOCUMENT) private _document, private cookieService: CookieService) { }

  ngOnInit() {
   this.displayChatBot();
  }

  ngAfterViewInit(){
    if(!this.cookieService.get('consent')){
      this.modalDirective.show();
    } 
  }

  scrollToTop(){
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  }

  displayChatBot(){
    const s = this.renderer2.createElement('script');
    s.type = 'text/javascript';
    s.src = './assets/chatbot.js';
    s.text = ``;
    this.renderer2.appendChild(this._document.body, s);
  }
  
  setConsentCookie(){
    if(!this.cookieService.get('consent')){
      this.cookieService.set('consent', 'consented');
    }
  }


}
