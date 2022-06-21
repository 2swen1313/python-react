import React from 'react';
import logo from './logo.svg';
import './App.css';
import ButtonItem from './components/Button.js'

import axios from 'axios'

const DOMAIN = 'http://127.0.0.1:8000'
const get_url = (url) => `${DOMAIN}${url}`


class App extends React.Component {
   constructor(props) {
       super(props)
       this.state = {
           button: []
       }
   }
   onbuttonPress()

   {
           axios.get('http://127.0.0.1:8000/api/button')
               .then(response => {
                   const button = response.data
                   this.setState(
                       {
                           'button': button
                       }
                   )
               }).catch(error => console.log(error))

   }
   render () {
       return (
           <div>
               <form name="search">
                   <div className="container">
                       <ButtonItem button={this.state.button}/>
                   </div>
                   <input type="text" name="key1" placeholder="Введите текст"></input>
                   {/*<button>onClick={onbuttonPress}</button>*/}
                   <input type="button" name="print2" value="показать"></input>
                   <input type="text" name="key2" value={this.state.field1}></input>


               </form>
           </div>
       )


   }
}

export default App;

