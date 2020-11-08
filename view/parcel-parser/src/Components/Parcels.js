import React, { Component } from "react";
import { withStyles } from "@material-ui/core/styles";
import {
  Table,
  TableHead,
  TableBody,
  TableCell,
  TableRow,
  Toolbar,
} from "@material-ui/core";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";
import config from "../Configs/config";

const styles = (theme) => ({
  root: {
    width: "100%",
    marginTop: theme.spacing(0.5),
    padding: 5,
    color: "white",
  },

  tableBodyContent: {
    padding: 5,
    backgroundColor: "#eeeeee",
  },

  head: {
    backgroundColor: "black",
    fontSize: 14,
    color: "white",
  },
  paper: {
    marginTop: "5px",
    background: "#eeeeee",
    width: "100%",
  },
  bodypaper: {
    marginTop: "5px",
    background: "#e8f5e9",
    width: "100%",
  },
  title: {
    flexGrow: 1,
    marginRight: theme.spacing(1),
  },
});
class MasterList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      packages: [],
    };
  }
  componentDidMount() {
    fetch(config.getPackageTypes, {
      method: "GET",
      credentials: "same-origin",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        credentials: "same-origin",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.packages);
        this.setState({
          packages: data.packages,
          dimensionsUnit: data.unit,
        });
      });

    fetch(config.weightLimit, {
      method: "GET",
      credentials: "same-origin",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        credentials: "same-origin",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.packages);
        this.setState({
          weightLimit: data.weightLimit,
          weightUnit: data.unit,
        });
      });
  }

  render() {
    const { classes } = this.props;
    const { packages, weightLimit, weightUnit, dimensionsUnit } = this.state;
    return (
      <div className={classes.root}>
        <Paper className={classes.paper}>
          <Toolbar>
            <Typography variant="h5" component="h3">
              Packages Available
            </Typography>
            <Typography
              variant="subtitle1"
              align="right"
              className={classes.title}
            >
              Weight Limit : {weightLimit} {weightUnit} <br />
              Dimensions are in ({dimensionsUnit})
            </Typography>
          </Toolbar>
        </Paper>
        <Paper className={classes.bodypaper}>
          <Table size="small">
            <TableHead className={classes.head}>
              <TableRow>
                <TableCell variant="head" className={classes.head}>
                  Package Type
                </TableCell>
                <TableCell variant="head" className={classes.head}>
                  Length
                </TableCell>
                <TableCell variant="head" className={classes.head}>
                  Breadth
                </TableCell>
                <TableCell variant="head" className={classes.head}>
                  Height
                </TableCell>
                <TableCell variant="head" className={classes.head}>
                  cost
                </TableCell>
              </TableRow>
            </TableHead>
            <TableBody className={classes.tableBodyContent}>
              {packages.map((item) => {
                return (
                  <TableRow key={item.type}>
                    <TableCell>{item.type}</TableCell>
                    <TableCell>{item.length}</TableCell>
                    <TableCell>{item.breadth}</TableCell>
                    <TableCell>{item.height}</TableCell>
                    <TableCell>{item.cost}</TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </Paper>
      </div>
    );
  }
}
export default withStyles(styles, { withTheme: true })(MasterList);
