import React, { Component } from 'react';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

class HomePage extends Component {
	render() {
		return (
			<Container style={{textAlign:"center"}}>
				<Row>
					<Col>
						<h1><b>Welcome!</b></h1>
					</Col>
				</Row>
				<hr />
				<Row className="justify-content-md-center">
					<Col>
						<h2>You have arrived at the website of <br /><i>aspiring software engineer</i>,<br /><i>competitive video game player</i>,<br /><i>and dog lover</i><br/><b>Nigel</b></h2>
					</Col>
				</Row>
				<hr />
				<Row>
					<Col>
						<h3>To learn more about me, visit the <a href="/about">About Tab</a>.</h3>
						<br />
						<h3>To learn more about my technical background, visit the <a href="/experience">Experience Tab</a></h3>
						<br />
						<h3>To read some more in-depth write ups of technical subjects, please visit the <a href="/blog">Blog Tab</a></h3>
						<br />
						<h3>To play a fun web game (and hopefully more in the future), visit the <a href="/games">Games Tab</a></h3>
					</Col>
				</Row>
			</Container>
		);
	}
}

export default HomePage;