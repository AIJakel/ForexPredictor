import React, { Component } from 'react';
import CandleStickStockScaleChart from "./components/ChartArea/Chart"
import axios from 'axios';
import './App.css';

const serverURL = 'http://127.0.0.1:5000/';
const http = axios.create({
  baseURL: serverURL,
});

//TODO: auto update predictions
// Add button row + interactions
// cacheing


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      activeChart: "",
      popen: "",
      pclose: "",
      phigh: "",
      plow: "",
      historical: null
    };
    this.test1 = this.getPrediction.bind(this);
    this.test2 = this.getHistorical.bind(this);
    this.datatf = this.formatData.bind(this);
    this.genChart = this.genChart.bind(this);
    this.renderCards = this.renderCards.bind(this);
  }

  componentDidMount() {
    this.getHistorical();
    this.getHistorical("usd_cad");
    this.getHistorical("eur_usd");
    this.getHistorical("gbp_usd");
    this.getHistorical("aud_usd");
    this.getHistorical("usd_chf");
    this.getHistorical("nzd_usd");
    this.getPrediction();
    this.getPrediction("usd_cad");
   // this.getPrediction("eur_usd");
    //this.getPrediction("gbp_usd");
   // this.getPrediction("aud_usd");
   // this.getPrediction("usd_chf");
   // this.getPrediction("nzd_usd");
  }

  getPrediction(pair="usd_jpy") {
    return (http.get("prediction/" + pair)
    .then((response) => this.setState({
      popen: response.data[0].p_open,
      pclose: response.data[0].p_close,
      phigh: response.data[0].p_high,
      plow: response.data[0].p_low
    }))
    .catch((err) => console.log(err)));
  }

  getHistorical(pair="usd_jpy") {
    return (http.get("historical/" + pair)
    .then((response) => this.formatData(response.data)) //call a function to parse the data
    .catch((err) => console.log(err)));
  }

  formatData(data){
    if(data !== undefined)
    {
      var final = [];
      for (var i = 0; i < 10000; i++) {
        var d = new Date(data[i].date);
        var o = data[i].open;
        var c = data[i].close;
        var h = data[i].high;
        var l = data[i].low;
        final.push ({date: d, open: o, close: c, high: h, low: l});
      }
      this.setState({historical: final});
    }
  }

  genChart(){
    const { historical } = this.state;
    if (historical !== null) {
      return(
        <CandleStickStockScaleChart
          data={historical}
          width={1200}
          ratio={5}
          type="svg"
        />
      );
    } 

    return (
      <div>
        Loading...
      </div>
    );
  }

  renderCards() {
    const { pclose, phigh, plow, popen } = this.state;
    if (pclose !== ""){
      return(
        <div className="main_card">
        <div className="header">
          Prediction for: 2017-12-08 12:00
        </div>
        <div className="open_card">
          <div className="value">{"$"+popen}</div>
          <div className="caption">OPEN</div>
        </div>
        <div className="close_card">
          <div className="value">{"$"+pclose}</div>
          <div className="caption">CLOSE</div>
        </div>
        <div className="high_card">
          <div className="value">{"$"+phigh}</div>
          <div className="caption">HIGH</div>
        </div>
        <div className="low_card">
          <div className="value">{"$"+plow}</div>
          <div className="caption">LOW</div>
        </div>
      </div>
      );
    }

    return(
      <div className="main_card">
        <div className="header">
          LOADING PREDICTION ...
        </div>
      </div>
    );
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.updateWindowDimensions);
  }


  render() {
    const { pclose, phigh, plow, popen } = this.state;
    return (
      <div className="App">
        <header className="App-header">

          <div className="title">
            FOREX Predictor
          </div>
          <div className="chart_title">
            USD/JPY
          </div>
          {this.genChart()}
          {this.renderCards()}
          

        </header>
      </div>
    );
  }
}

export default App;

//this.setState({t: response.data.P_})






// import React from 'react';
// import { render } from 'react-dom';
// import Chart from './components/ChartArea/Chart';
// import { getData } from "./components/ChartArea/utils"

// class ChartComponent extends React.Component {
// 	componentDidMount() {
// 		getData().then(data => {
// 			this.setState({ data })
// 		})
// 	}
// 	render() {
// 		if (this.state == null) {
// 			return <div>Loading...</div>
// 		}
// 		return (
//       <Chart data={this.state.data} />
// 		)
// 	}
// }

// render(
// 	<ChartComponent />,
// 	document.getElementById("root")
// );

// export default ChartComponent;
