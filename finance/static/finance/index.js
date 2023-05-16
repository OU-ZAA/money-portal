document.addEventListener("DOMContentLoaded", () => {
    displayBalance()
    displayMonthlyDepositAndSpending()
    document.querySelector("form").addEventListener("submit", async (e) => {
        e.preventDefault()

        try {
            // Hittin the api to save the transation in db
            await fetch("/transactions", {
                method: "post",
                body: JSON.stringify({
                    amount: document.querySelector("#amount").value,
                    transaction_type: document.querySelector("#transaction-type").value,
                    memo: document.querySelector("#memo").value
                })
            })
        } catch (e) {
            console.error(e)
        }

        // Clear the form
        document.querySelector("#amount").value = ""
        document.querySelector("#transaction-type").value = ""
        document.querySelector("#memo").value = ""

        load_dashboard()
        displayBalance()
        displayMonthlyDepositAndSpending()
    })

    load_dashboard()
})

async function load_dashboard() {
    try {
        res = await fetch("/transactions")
        data = await res.json()
        
        // Meke sure transactions exists
        if (data.length === 0) return

        document.querySelector("tbody").innerHTML = ""
        data.map(transaction => {
            
            // Create a table row element
            const transactionRow = document.createElement("tr")

            // Create table data element for every element in the transaction
            const amountDiv = document.createElement("td")
            const transactionTypeDiv = document.createElement("td")
            const memoDiv = document.createElement("td")
            const createdAtDiv = document.createElement("td")

            // Add the transaction content to its specific div
            amountDiv.textContent = `$${transaction.amount}`
            transactionTypeDiv.textContent = transaction.transaction_type
            memoDiv.textContent = transaction.memo
            createdAtDiv.textContent = transaction.created_at

            transactionRow.append(amountDiv, memoDiv, transactionTypeDiv, createdAtDiv)
            document.querySelector("tbody").append(transactionRow)

            if (transaction.transaction_type === "deposit") {
                transactionTypeDiv.classList.add("text-success")
                amountDiv.classList.add("text-success")
            } else if (transaction.transaction_type === "point of sale") {
                transactionTypeDiv.classList.add("text-danger")
                amountDiv.classList.add("text-danger")
            }
        }) 

        // Update the transactions count
        document.querySelector("#transactions").textContent = data.length
        
    } catch (e) {
        console.error(e)
    }
}

async function displayBalance() {
    // The the current login user balance
    res = await fetch("/users")
    data = await res.json()

    // Render the balance in the ui
    document.querySelector("#balance").textContent = `$${data.balance}`
}

async function displayMonthlyDepositAndSpending() {
    // Fetch the monthly spending
    res = await fetch("/transactions/thismonth")
    data = await res.json()

    // Calculate the monthly deposit and spending
    let monthlyDeposit = 0
    let monthlySpending = 0
    data.map(transaction => {
        if (transaction.transaction_type === "deposit") {
            monthlyDeposit += transaction.amount
        } else if (transaction.transaction_type === "point of sale") {
            monthlySpending += transaction.amount
        }
    })

    // Rendet the result
    document.querySelector("#monthly-spending").textContent = `$${monthlySpending}`
    document.querySelector("#monthly-deposit").textContent = `$${monthlyDeposit}`
}