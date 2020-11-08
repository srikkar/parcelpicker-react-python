import React, { Component } from "react";
import { withStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import { Grid } from "@material-ui/core";

const styles = (theme) => ({
  root: {
    flexGrow: 1,
    minWidth: "270px",
  },
  AppBar: {
    backgroundColor: "black",
  },
  title: {
    flexGrow: 1,
    color: "white",
    marginRight: theme.spacing(1),
  },
});
class ButtonAppBar extends Component {
  render() {
    const { classes } = this.props;

    return (
      <div className={classes.root}>
        <AppBar position="static" className={classes.AppBar}>
          <Grid container>
            <Grid item md={1} className={classes.gridcss}></Grid>
            <Grid item md={10}>
              <Toolbar>
                <Typography
                  variant="h4"
                  className={classes.title}
                  display="block"
                >
                  TradeMe
                </Typography>
              </Toolbar>
            </Grid>
            <Grid item md={1} className={classes.gridcss}></Grid>
          </Grid>
        </AppBar>
      </div>
    );
  }
}
export default withStyles(styles, { withTheme: true })(ButtonAppBar);
