from pyscript import document  # pyright: ignore[reportMissingImports]
def compute_average(event):
    # Get the input values and convert to float
    score1 = float(document.getElementById("score1").value)
    score2 = float(document.getElementById("score2").value)

    # Compute average
    average = (score1 + score2) / 2

    # Determine pass or fail
    if average >= 75:
        result = "Pass"
    else:
        result = "Fail"

    # Display results
    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result