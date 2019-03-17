import React from 'react';
//import { render } from 'react-dom';
import Chart from './Chart';
//import { getData } from "./utils"


class ChartComponent extends React.Component {
	render() {
    const {Data} = this.props;
    console.log(Data);
		if (Data == null || Data === undefined) {
			return <div>Loading...</div>
		}
		return (
		  <Chart data={Data} />
		)
	}
}

/*
render(
	<ChartComponent />,
	document.getElementById("root")
);
*/

export default ChartComponent;
