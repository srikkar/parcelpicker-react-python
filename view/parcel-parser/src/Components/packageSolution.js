import React, { Component } from "react";
import { withStyles } from "@material-ui/core/styles";
import { Toolbar } from "@material-ui/core";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";
import Fade from "@material-ui/core/Fade";
import Button from "@material-ui/core/Button";
import { Grid } from "@material-ui/core";

import Card from "@material-ui/core/Card";
import CardActionArea from "@material-ui/core/CardActionArea";
import CardActions from "@material-ui/core/CardActions";
import CardContent from "@material-ui/core/CardContent";
import CardMedia from "@material-ui/core/CardMedia";

const styles = (theme) => ({
  root: {
    width: "100%",
    flexGrow: 5,
    paddingTop: "inherit",
    marginTop: "15px",
  },

  paper: {
    marginTop: "15px",
    width: "auto",
    backgroundColor: "lightgray",
  },
  bodypaperException: {
    marginTop: "5px",
    background: "lightcoral",
    width: "100%",
  },
  bodypaperPackage: {
    marginTop: "5px",
    background: "lightblue",
    width: "100%",
  },
  title: {
    flexGrow: 1,
    marginRight: theme.spacing(1),
  },
  media: {
    height: 140,
  },
  gridcss: {
    margin: 10,
  },
});
class MasterList extends Component {
  constructor(props) {
    super(props);
    this.state = {
        viewPackages: false
    }
    this.buttonClick = this.buttonClick.bind(this)
  }

    buttonClick = (value) => {   
        
        this.props.updateViewPackages(value)
        this.setState({
            viewPackages: value
        })

    
    }
  render() {
    const { classes, shared_details } = this.props;
    const detailsFound = Object.keys(shared_details).length > 0 ? true : false;
    const exceptionFound = shared_details.exception;
    console.log(shared_details);

    return (
      <Fade in={detailsFound}>
        <Card className={classes.root}>
          <CardActionArea>
            <CardMedia
              className={classes.media}
              image="./package-solution/whitePackages.jpg"
              title="Package"
            />
            <CardContent>
              <Paper
                className={classes.paper}
                style={
                  detailsFound ? { display: "block" } : { display: "none" }
                }
              >
                <Toolbar>
                  <Typography
                    variant="h6"
                    className={classes.title}
                    display="block"
                  >
                    Package Suggestion
                  </Typography>
                </Toolbar>
              </Paper>
              <Paper
                className={classes.bodypaperException}
                style={
                  exceptionFound !== null
                    ? { display: "block" }
                    : { display: "none" }
                }
              >
                <Toolbar>
                  <Typography variant="h6" className={classes.title}>
                    {shared_details.exception}
                  </Typography>
                </Toolbar>
              </Paper>
              <Grid container>
                <Grid item md={4} className={classes.gridcss}>
                  <Paper
                    className={classes.bodypaperPackage}
                    style={
                      exceptionFound === null
                        ? { display: "block" }
                        : { display: "none" }
                    }
                  >
                    <Toolbar>
                      <Typography variant="h6" className={classes.title}>
                        {shared_details.packageType}
                      </Typography>
                    </Toolbar>
                  </Paper>
                </Grid>
                <Grid item md={2} className={classes.gridcss}>
                  {" "}
                </Grid>
                <Grid item md={4} className={classes.gridcss}>
                  <Paper
                    className={classes.bodypaperPackage}
                    style={
                      exceptionFound === null
                        ? { display: "block" }
                        : { display: "none" }
                    }
                  >
                    <Toolbar>
                      <Typography variant="h6" className={classes.title}>
                        {shared_details.cost}
                      </Typography>
                    </Toolbar>
                  </Paper>
                </Grid>
              </Grid>
            </CardContent>
          </CardActionArea>
          <CardActions>
            <Button size="small" color="primary" onClick={this.state.viewPackages ? () => this.buttonClick(false) : () => this.buttonClick(true) }>
                {this.state.viewPackages ? "Hide" : "know more" }
            </Button>
          </CardActions>
        </Card>
      </Fade>
    );
  }
}
export default withStyles(styles, { withTheme: true })(MasterList);
