import React, { Component } from 'react';
import PropTypes from "prop-types";
import  "./ButtonList.css";

class ButtonList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      active: null,
    }
    this.renderButton = this.renderButton.bind(this);
    this.click = this.click.bind(this);
  }

  renderButton(caption, index, action) {
    return(
      <button color="primary" key={index} id={caption} className="button" onClick={action}>
        {caption}
      </button>
    );
  }

  click(e,x){
    console.log(e.target.id);
    console.log(x);
  }

  render(){
    const { buttons, action } = this.props;
    return (
      <div className="button_list">

        {buttons.map((item, index) => {
          return(this.renderButton(item, index, action));
        })}

      </div>
    );
  }

}

ButtonList.propTypes = {
  buttons: PropTypes.array.isRequired,
  action: PropTypes.func.isRequired
};

export default ButtonList;