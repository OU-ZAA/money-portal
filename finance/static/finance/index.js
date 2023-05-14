document.addEventListener("DOMContentLoaded", () => {
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
    })
})

function load_dashboard() {
    
}