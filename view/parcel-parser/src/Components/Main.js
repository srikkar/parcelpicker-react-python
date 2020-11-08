import React, { Component } from "react";
import { withStyles } from "@material-ui/core/styles";
import Search from "./Search";
import PackageSolution from "./packageSolution";
import Parcels from "./Parcels";
import ButtonAppBar from "./AppBar";
import { Grid } from "@material-ui/core";

const styles = (theme) => ({
  root: {
    width: "100%",
    flexGrow: 5,
    paddingTop: "inherit",
  },
  gridcss: {
    margin: 10,
  },
});

class Main extends Component {
  constructor(props) {
    super(props);
    this.state = {
      shared_details: {},
      viewPackages: false,
    };
    this.updateSharedDetails = this.updateSharedDetails.bind(this);
    this.updateViewPackages = this.updateViewPackages.bind(this);
  }

  updateSharedDetails(shared_value) {
    console.log(shared_value);
    this.setState({ shared_details: shared_value });
  }
  updateViewPackages(shared_value) {
    console.log(shared_value);
    this.setState({ viewPackages: shared_value });
  }
  render() {
    const { classes } = this.props;
    console.log(this.state.viewPackages);
    return (
      <div className="App">
        <ButtonAppBar />
        <Grid container>
          <Grid item md={1} className={classes.gridcss}></Grid>

          <Grid item md={5} className={classes.gridcss}>
            <Search updateSharedDetails={this.updateSharedDetails} />
          </Grid>

          <Grid item md={5} className={classes.gridcss}>
            <PackageSolution
              shared_details={this.state.shared_details}
              updateViewPackages={this.updateViewPackages}
            />
          </Grid>

          {this.state.viewPackages ? (
            <Grid container>
              <Grid item md={1} className={classes.gridcss}></Grid>
              <Grid item md={10} className={classes.gridcss}>
                <Parcels />
              </Grid>
              <Grid item md={1} className={classes.gridcss}></Grid>

              <Grid item md={1} className={classes.gridcss}></Grid>
            </Grid>
          ) : null}
        </Grid>
      </div>
    );
  }
}

export default withStyles(styles, { withTheme: true })(Main);
