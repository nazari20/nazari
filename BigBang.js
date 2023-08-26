let template = document.createElement('template');
template.innerHTML = `
<div>
    <h2>Big Bang theory</h2>
</div>
`;

class BigBang extends HTMLElement{
  constructor(){
    super();
    const shadowRoot = this.attachShadow({mode: 'closed'});
    //let div = document.createElement('div');
    //div.textContent = 'Big Bang theory';
    //shadowRoot.append(div);

    let clone = template.content.cloneNode(true);
    shadowRoot.append(clone);
  }
}

customElements.define('big-bang', BigBang);