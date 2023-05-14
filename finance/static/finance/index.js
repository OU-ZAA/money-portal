document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("form").addEventListener("submit", (e) => {
        e.preventDefault()

        // Hittin the api to save the transation in db
        fetch("/transactions", {
            method: "post",
            body: JSON.stringify({
                amount: document.querySelector("#amount").value,
                transaction_type: document.querySelector("#transaction-type").value,
                memo: document.querySelector("#memo").value
            })
        })
    })
})