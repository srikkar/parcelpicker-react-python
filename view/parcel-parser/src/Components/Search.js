import React, { Component } from "react";
import { withStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import Paper from "@material-ui/core/Paper";
import config from "../Configs/config";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";

const numberPattern = new RegExp("^[0-9.]+$");

const styles = (theme) => ({
  root: {
    display: "flex",
    paddingTop: "inherit",
  },
  container: {
    position: "relative",
  },
  gridcss: {
    margin: 10,
  },
  paper: {
    marginTop: "15px",
    width: "100%",
    padding: theme.spacing(3),
    color: theme.palette.text.secondary,
    backgroundColor: "#eeeeee",
  },
  button: {
    backgroundColor: "lightslategray",
    color: "#ffffff",
  },
  title: {
    flexGrow: 1,
    marginRight: theme.spacing(1),
  },
});

class Search extends Component {
  constructor(props) {
    super(props);

    this.state = {
      length: "",
      breadth: "",
      height: "",
      weight: "",
      lengthError: "",
      breadthError: "",
      heightError: "",
      weightError: "",
      disabled: true,
      resetDisable: true,
    };

    this.handleChange = this.handleChange.bind(this);

    this.buttonClick = this.buttonClick.bind(this);
    this.resetClick = this.resetClick.bind(this);
  }

  handleChange = (name) => (event) => {
    let val = event.target.value;
    this.setState({
      [name]: val,
    });
  };
  getClearState() {
    return {
      length: "",
      breadth: "",
      height: "",
      weight: "",
      disabled: true,
      resetDisable: true,
    };
  }

  resetClick = () => {
    this.setState({
      ...this.getClearState(),
    });
    this.props.updateSharedDetails({});
  };

  handleBlur = (name) => (event) => {
    let val = event.target.value;
    numberPattern.test(val) || val === ""
      ? this.setState({ [name]: "" })
      : this.setState({ [name]: "enter Number" });

    let {
      lengthError,
      breadthError,
      heightError,
      weightError,
      length,
      breadth,
      height,
      weight,
    } = this.state;

    breadthError === "" &&
    weightError === "" &&
    heightError === "" &&
    lengthError === "" &&
    length !== "" &&
    breadth !== "" &&
    weight !== "" &&
    height !== ""
      ? this.setState({ disabled: false })
      : this.setState({ disabled: true, resetDisable: false });
  };

  buttonClick = () => {
    console.log(this.state);
    var requestObject = { length: "", breadth: "", height: "", weight: "" };
    Object.keys(requestObject).map(
      (item) => (requestObject[item] = parseFloat(this.state[item]))
    );
    fetch(config.packageSolution, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        credentials: "same-origin",
      },
      body: JSON.stringify(requestObject),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        this.props.updateSharedDetails(data);
        if (Object.keys(data).length === 0) {
          alert("PackageTypes Not Available");
        }
      });
  };

  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <Paper className={classes.paper} variant="outlined" elevation={3}>
          <Typography variant="h6" className={classes.title} display="block">
            Packaging Solutions
          </Typography>

          <Grid item md={12} className={classes.gridcss}>
            <TextField
              id="outlined-breadth-helper-text"
              label="Length"
              onBlur={this.handleBlur("lengthError")}
              value={this.state.length}
              onChange={this.handleChange("length")}
              helperText={this.state.lengthError}
              variant="outlined"
            />
          </Grid>
          <Grid item md={12} className={classes.gridcss}>
            <TextField
              id="outlined-breadth-helper-text"
              label="Breadth"
              onBlur={this.handleBlur("breadthError")}
              value={this.state.breadth}
              onChange={this.handleChange("breadth")}
              helperText={this.state.breadthError}
              variant="outlined"
            />
          </Grid>
          <Grid item md={12} className={classes.gridcss}>
            <TextField
              id="outlined-breadth-helper-text"
              label="Height"
              onBlur={this.handleBlur("heightError")}
              value={this.state.height}
              onChange={this.handleChange("height")}
              helperText={this.state.heightError}
              variant="outlined"
            />
          </Grid>
          <Grid item md={12} className={classes.gridcss}>
            <TextField
              id="outlined-breadth-helper-text"
              label="Weight"
              onBlur={this.handleBlur("weightError")}
              value={this.state.weight}
              onChange={this.handleChange("weight")}
              helperText={this.state.weightError}
              variant="outlined"
            />
          </Grid>
          <Grid container className={classes.root}>
            <Grid item md={2} className={classes.gridcss}>
              <Button
                variant="contained"
                color="default"
                onClick={() => this.buttonClick()}
                disabled={this.state.disabled}
                className={classes.button}
              >
                Submit
              </Button>
            </Grid>

            <Grid item md={2} className={classes.gridcss}>
              <Button
                variant="contained"
                color="default"
                onClick={() => this.resetClick()}
                disabled={this.state.resetDisable}
                className={classes.button}
              >
                Reset
              </Button>
            </Grid>
            <Grid item md={8} className={classes.gridcss}></Grid>
          </Grid>
        </Paper>
      </div>
    );
  }
}

export default withStyles(styles, { withTheme: true })(Search);
