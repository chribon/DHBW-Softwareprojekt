import { Component, OnInit, Renderer2, Inject } from '@angular/core';
import { DOCUMENT } from '@angular/common';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.css']
})
export class FooterComponent implements OnInit {

  constructor(private renderer2: Renderer2, @Inject(DOCUMENT) private _document) { }

  ngOnInit() {
   this.displayChatBot();
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

}
