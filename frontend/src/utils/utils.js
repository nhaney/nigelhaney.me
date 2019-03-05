function formatDate(date) {
	var curDate = date.getDate();
	curDate = curDate < 10 ? "0" + curDate : curDate;

	var curMonth = date.getMonth() + 1;
	curMonth = curMonth < 10 ? "0" + curMonth : curMonth;

	let curYear = date.getFullYear();

	var curHour = date.getHours();
	var curMin = date.getMinutes();
	curMin = curMin < 10 ? '0' + curMin : curMin;
	var ampm = curHour >= 12 ? 'pm' : 'am';

	curHour = curHour % 12;
	curHour = curHour ? curHour : 12;

	let strTime = curHour + ':' + curMin + ' ' + ampm;

	return curMonth + "/" + curDate + "/" + curYear + " at " + strTime;
}

function dateConverter(timeStamp) {
	if (!timeStamp) {
		return;
	}
	let timeSplit = timeStamp.split(" ");
	let date = new Date(
		Date.parse(timeSplit[0] + 'T' + timeSplit[1] + 'Z')
	);

	return formatDate(date);
};

export default dateConverter;