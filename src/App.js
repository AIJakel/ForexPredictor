import React, { Component } from 'react';
import CandleStickStockScaleChart from "./components/Chart/Chart";
import ButtonList from "./components/ButtonList/ButtonList";
import axios from 'axios';
import './App.css';

const serverURL = 'http://127.0.0.1:5000/';
const http = axios.create({
  baseURL: serverURL,
});

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      activeChart: "usd_jpy",
      popen: "",
      pclose: "",
      phigh: "",
      plow: "",
      historical: null,
      pusd_jpy: null,
      pusd_cad: null,
      peur_usd: null,
      pgbp_usd: null,
      paud_usd: null,
      pusd_chf: null,
      pnzd_usd: null,

    };
    this.test1 = this.getPrediction.bind(this);
    this.test2 = this.getHistorical.bind(this);
    this.datatf = this.formatData.bind(this);
    this.genChart = this.genChart.bind(this);
    this.renderCards = this.renderCards.bind(this);
    this.formatPrediction = this.formatPrediction.bind(this);
    this.buttonClick = this.buttonClick.bind(this);
    this.getDate = this.getDate.bind(this);
  }

  componentDidMount() {
    this.getHistorical();
    this.getPrediction();
  }

  getPrediction(pair="usd_jpy") {
    return (http.get("prediction/" + pair)
    .then((response) => this.formatPrediction(response.data, pair)))
    .catch((err) => console.log(err));
  }

  getHistorical(pair="usd_jpy") {
    return (http.get("historical/" + pair)
    .then((response) => this.formatData(response.data))
    .catch((err) => console.log(err)));
  }

  getDate(pair="usd_jpy"){
    return (http.get("getDate/" + pair)
    .then((response) => this.formatDate(response.data))
    .catch((err) => console.log(err)));
  }

  formatDate(date){
    if (date !== undefined) {
      var options = {};
      var tmp = new Date(data[0].date);
      var d = tmp.toLocaleDateString("en-US", options);
      this.setState({date: d});
    }
  }

  formatPrediction(response, pair) {
    if(response !== undefined) 
    {
      var x = "p"+pair
      this.setState({
        [x]: {open: response[0].p_open, close: response[0].p_close, high: response[0].p_high, low: response[0].p_low}
      });
    }
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

  renderCards(chart) {
    var x = "p"+chart
    if (this.state[x] !== null){
      return(
        <div className="main_card">
        <div className="header">
          {"Prediction for: "+2017-12-08 12:00}
        </div>
        <div className="open_card">
          <div className="value">{"$"+this.state[x].open}</div>
          <div className="caption">OPEN</div>
        </div>
        <div className="close_card">
          <div className="value">{"$"+this.state[x].close}</div>
          <div className="caption">CLOSE</div>
        </div>
        <div className="high_card">
          <div className="value">{"$"+this.state[x].high}</div>
          <div className="caption">HIGH</div>
        </div>
        <div className="low_card">
          <div className="value">{"$"+this.state[x].low}</div>
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

  buttonClick(e) {
    var pair = e.target.id.toLowerCase().replace("/", "_");
    this.setState({activeChart: pair});
    this.getHistorical(pair);

    var ppair = "p"+pair;
    if (this.state[ppair] === null) {

      this.getPrediction(pair);
    }
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.updateWindowDimensions);
  }

  render() {
    const { activeChart } = this.state;
    return (
      <div className="App">
        <header className="App-header">
          <div className="title">
            FOREX Predictor
          </div>
          <ButtonList
            buttons={["USD/JPY","USD/CAD","EUR/USD","GBP/USD","AUD/USD","USD/CHF","NZD/USD"]}
            action={this.buttonClick}
          />
          <div className="chart_title">
            {activeChart.toUpperCase().replace("_", "/")}
          </div>
          {this.genChart()}
          {this.renderCards(activeChart)}
          
        </header>
      </div>
    );
  }
}

export default App;