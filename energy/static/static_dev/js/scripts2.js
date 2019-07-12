    let globUrlZone = "https://6cf02177.ngrok.io/getzone/73/";

    let headers = new Headers();

    headers.append("Content-Type", "application/json");
    headers.append("Accept", "application/json");
    headers.append("Access-Control-Allow-Origin", "https://6cf02177.ngrok.io/getzone/73/");



async function getData(url) {
        let dataJson = {};
        dataJson = await fetch(url,
            {
                headers: headers,
                method: "GET",
                mode: "cors"
            })

            .then(
                function (response) {
                    if (response.status == 200) {

                    }
                    if (response.status !== 200) {
                        console.log("Request has a problem. Status Code: " + response.status);
                        return;
                    }

                    // Return request and parse
                    return response.json();
                })
            .then(function (data) {
                console.log(data);


            });
        return dataJson
    };

getData(globUrlZone + 3 +'/');