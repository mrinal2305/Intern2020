import React, { Component } from "react";
import styles from "./Home.module.css";
import cloudDB, { collectionName } from "../../services/firebase";
import LineChart from "../charts/LineChart/LineChart";

class Home extends Component {
    state = {
        data: [],
    };
    async componentDidMount() {
        let sentimentData = [];
        try {
            await cloudDB.collection(collectionName).get().then((querySnapshot) => {
                querySnapshot.forEach((doc) => {
                    sentimentData.push(
                        {
                            date: doc.id,
                            value: doc.data()
                        }
                    );
                });
            });
        } catch (error) {
            console.log(error);

        }
        this.setState({ data: sentimentData });
    }
    render() {
        const { data } = this.state;
        const h = this.state.data.length !== 0 ? (<div className={styles.Charts}>
            {/* <LineChart title="Joy" sentiment={data} />
            <BarChart title="Joy" sentiment={data} />
            <PieChart sentiment={data} /> */}
            <LineChart sentiment={data.map(d => { return { x: d.value.joy, y: d.date } })} />
        </div>) : null;
        return (
            <>
                <div className={styles.Container}>
                    <h1>Daily Data</h1>
                    {h}
                </div>
            </>
        );
    }
}

export default Home;