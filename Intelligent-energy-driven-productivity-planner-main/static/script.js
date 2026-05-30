async function analyzeProductivity(){

    const data = {

        sleep:
        document.getElementById('sleep').value,

        stress:
        document.getElementById('stress').value,

        work_hours:
        document.getElementById('work_hours').value,

        mood:
        document.getElementById('mood').value
    };

    const response = await fetch('/analyze',{

        method:'POST',

        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById('results').innerHTML = `

    <div class="result-box">

        <h2>
            ⚡ Energy Level: ${result.energy}%
        </h2>

        <br>

        <h2>
            🔥 Burnout Risk: ${result.burnout}%
        </h2>

        <br>

        <p>
            ${result.recommendation}
        </p>

    </div>
    `;
}