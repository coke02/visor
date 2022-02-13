const data = {
    labels: [
        'N',
        'NE',
        'E',
        'SE',
        'S',
        'SO',
        'O',
        'NO'
    ],
    datasets: [{
        label: 'Viento',
        data: [89, 50, 40, 6, 0, 0, 0, 14],
        fill: true,
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgb(255, 99, 132)',
        pointBackgroundColor: 'rgb(255, 99, 132)',
        pointBorderColor: '#fff',
        pointHoverBackgroundColor: '#fff',
        pointHoverBorderColor: 'rgb(255, 99, 132)'
    }]
};

const config = {
    type: 'radar',
    data: data,
    options: {
        elements: {
        line: {
            borderWidth: 3
        }
        }
    },
};
