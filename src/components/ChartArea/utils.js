import { tsvParse, csvParse } from  "d3-dsv";
import { timeParse } from "d3-time-format";

function parseData(parse) {
	return function(d) {
		d.date = parse(d.date);
		d.open = +d.open;
		d.high = +d.high;
		d.low = +d.low;
		d.close = +d.close;

		return d;
	};
}

const parseDate = timeParse("%Y-%m-%d");

export function getData() {
	const promise = fetch("https://cdn.rawgit.com/rrag/react-stockcharts/master/docs/data/MSFT.tsv")
    .then(response => response.text())
    .then(data => tsvParse(data, parseData(parseDate)))
	return promise;
}
