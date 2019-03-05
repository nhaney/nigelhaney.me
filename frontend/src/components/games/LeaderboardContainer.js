import React, { Component } from 'react';

import Dropdown from 'react-bootstrap/Dropdown';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';

import axios from 'axios';

import HighScoreTable from './HighScoreTable';

class LeaderboardContainer extends Component {
	constructor(props) {
		super(props);

		this.state = {
			scores: [],
			isLoading: true,
			game_name: this.props.match.params.game_name
		}
	};

	componentWillMount() {
		axios.get("https://nigelhaney.me/api/game/" + this.state.game_name)
		.then(
			res => {
				this.setState({scores: res.data.data,
							   isLoading: false});
			});
	};

	gameTitleComponent() {
		if (this.state.game_name === "fish") {
			return (<h2 style={{textAlign:"center"}}>High Scores:<br /> Stay Off The Line!</h2>);
		}
		else {
			return (<h2 style={{textAlign:"center"}}>Leaderboard not found</h2>);
		}
	};

	dropDownComponent() {
		return(
				<Dropdown>
						<Dropdown.Toggle>
							Select Leaderboard
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item disabled={this.state.game_name === "fish" && true} href="/games/scores/fish">Stay Off The Line</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
			)
	}

	render() {
		return (
			<Container>
				<Row>
					<Col>
						<h1 style={{textAlign:"center"}}><b>Game Leaderboards</b></h1>
					</Col>
				</Row>
				<hr />
				<Row className="justify-content-sm-center">
					<Col sm={4}>
						{this.gameTitleComponent()}	
					</Col>
				</Row>
				<Row>
					<Col sm={4}>
						<Button className="text-xs-right" href={"https://nigelhaney.me/games/" + this.state.game_name}>Play</Button>
					</Col>
					<Col sm={{span:4, offset:4, textAlign:"right"}} style={{textAlign:"end"}}>
						{this.dropDownComponent()}
					</Col>
				</Row>
				<hr />
				<Row>
					<HighScoreTable data={this.state.scores}/>
				</Row>

			</Container>
		);
	}
}

export default LeaderboardContainer;