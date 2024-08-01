import React, { Component } from "react";
import { render } from "react-dom";
import Homepage from "./homepage";
import RoomJoinPage from "./RoomJoinPage";
import CreateRoomPage from "./createRoomPage";

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render(){
        return(<div>
        <Homepage></Homepage>
        </div>
    );
    }
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);