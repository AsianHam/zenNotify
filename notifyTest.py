import React from 'react';
import { render } from 'react-dom';
import { ToastContainer, toast } from "react-toastify";

const styles = {
  fontFamily: 'sans-serif',
  textAlign: 'center',
};

const linkStyle = {
 border: "1px solid",
 color: "#fff",
 background: "black",
 padding: "5px"
}; 

class NewMessageNotification extends React.Component {
  
  displayMessage = () => {
    //remove all notifications
    toast.dismiss();

    //navigate to the link. I'll use location hash but it can be done with any router solution
    window.location.hash = this.props.link;
  }

  render(){
    return (
      <div>
        New Message <a style={linkStyle} onClick={this.displayMessage}>View message</a>
      </div>
    );
  }
}



class App extends React.Component{

  play = () => {
    ['#link1', '#link2', '#link3'].forEach( link => {
      toast(<NewMessageNotification link={link} />);
    });
  }  

  render(){
    return (
      <div style={styles}>

        <h2>Start editing to see some magic happen {'\u2728'}</h2>
        <button onClick={this.play}>Play Scenario </button>
        <ToastContainer />
      </div>
    );
  }
}

render(<App />, document.getElementById('root'));
