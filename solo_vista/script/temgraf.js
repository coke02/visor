
  $(document).ready(function () {
    const config = {
        type: 'line',
        data: {
            labels: [],
            datasets: [{
                label: "Temperatura",
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [],
                fill: false,
               

            },
        ]},

        options: {
            responsive: true,
            title: {
                display: true,
                text: "Gráfico de Temperatura" 
                
            },
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: {
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Fecha'
                    }
                },
                yAxes: {
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Velocidad en Mbps'
                    },

                },
            }
        }
    };

    const context = document.getElementById('canvas').getContext('2d');

    const lineChart = new Chart(context, config);

    const source = new EventSource("/chart-data");

    source.onmessage = function (event) {
        const data = JSON.parse(event.data);
        if (config.data.labels.length === 20) {
            config.data.labels.shift();
            config.data.datasets[0].data.shift();
            config.data.datasets[1].data.shift();
           
        }
        config.data.labels.push(data.time);
        config.data.datasets[0].data.push(data.value);
        config.data.datasets[1].data.push(data.value1);
        lineChart.update();
    }
});
