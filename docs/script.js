function calculateBMI() {
    var weight = document.getElementById("weight").value;
    var height = document.getElementById("height").value;

    if(weight && height){
        var bmi = (weight / ((height / 100) ** 2)).toFixed(2);
        var category = "";

        if (bmi < 18.5)
            category = "Underweight";
        else if (bmi < 24.9)
            category = "Normal";
        else if (bmi < 29.9)
            category = "Overweight";
        else
            category = "Obese";

        document.getElementById("result").innerText = "Your BMI is " + bmi + " (" + category + ")";
    } else {
        alert("Please enter both weight and height!");
    }
}
