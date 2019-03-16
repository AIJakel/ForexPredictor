import React from 'react';
import { render } from 'react-dom';
import Chart from './components/ChartArea/Chart';
import { getData } from "./components/ChartArea/utils"

class ChartComponent extends React.Component {
	componentDidMount() {
		getData().then(data => {
			this.setState({ data })
		})
	}
	render() {
		if (this.state == null) {
			return <div>Loading...</div>
		}
		return (
      <Chart data={this.state.data} />
		)
	}
}

render(
	<ChartComponent />,
	document.getElementById("root")
);

export default ChartComponent;
