let config = {}
if (process.env.NODE_ENV === "production") {
    config.packageSolution = "/parseTheParcel/packageSolution"
    config.getPackageTypes = "/parseTheParcel/packageTypes"
    config.weightLimit = "/parseTheParcel/weightLimit"
    config.dimesionErrorText = "Please enter number"
    
}
else {
    config.packageSolution = "http://127.0.0.1:8001/parseTheParcel/packageSolution"
    config.getPackageTypes = "http://127.0.0.1:8001/parseTheParcel/packageTypes"
    config.weightLimit = "http://127.0.0.1:8001/parseTheParcel/weightLimit"
    config.dimesionErrorText = "Please enter number"
}

export default config;