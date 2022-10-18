const urlEncoder = paramObj => {
	let arr = [];
	
	for(key in paramObj){
		let param = key + '=' + encodeURIComponent(paramObj[key]);
		arr.push(param);
	}
	return arr.join('&'); //a=b&가=나&t=q
}

async function postData(url = '', data = {}) {
    const response = await fetch(url, {
        method: 'POST',
        mode: 'cors', // no-cors, *cors, same-origin
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), 
    });

    return response.json(); 
}

async function getData(url = '', data = {}, header = {'Content-Type': 'application/json'}) {

    url += '?' + urlEncoder(data)

    const response = await fetch(url, {
        method: 'GET',
        mode: 'cors', // no-cors, *cors, same-origin
        credentials: 'same-origin', // include, *same-origin, omit
        headers: header,        
    });

    return response.json(); 
}

function stdDayToString(stdDay){
    month = stdDay.getMonth() >= 10 ? stdDay.getMonth() : '0'+ stdDay.getMonth()
    day = stdDay.getDate() >= 10 ? stdDay.getDate() : '0'+ stdDay.getDate()
    return stdDay.getFullYear()+ '-' + month + '-' + day
}
