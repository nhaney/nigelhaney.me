import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Media from 'react-bootstrap/Media';
import Button from 'react-bootstrap/Button';

class GamePreviewContainer extends Component {
	render() {
		return (
			<Container>
				<Row className="justify-content-md-center">
					<Col>
						<h1 style={{textAlign: "center"}}><b>My Game Collection</b></h1>
					</Col>
				</Row>
				<hr />
				<Row className="justify-content-md-center">
					<Col>
						<p>One of my favorite things to do is make games. In this section of my site I will host a collection of games I have made.</p>
					</Col>
				</Row>
				<hr />
				<span style={{display:"block"}}>
					<Row className="justify-content-md-center">
						<Media>	
								<img 
									width={122}
									height={122}
									className="mr-3"
									src={require("../../imgs/fish_preview.jpg")}
									alt="fish game"
								/>
								<Media.Body>
									<h5>Stay off the Line!</h5>
									<p>
										Game where you play as a tasty fish trying to survive in the ocean. Try to last as long as you can, and most importantly, Stay Off the Line!
										<br />
										<i>(Not mobile friendly)</i>
									</p>

									<Button href="https://nigelhaney.me/games/fish" style={{margin:"10px"}}>Play</Button>
									<Link to="/games/scores/fish" style={{color:"black", textDecoration:"none"}}>
										<Button style={{margin:"10px"}}>Leaderboards</Button>
									</Link>
								</Media.Body>
						</Media>
					</Row>
				</span>
			</Container>
		);
	}
}

export default GamePreviewContainer;