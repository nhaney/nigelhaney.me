import React, { Component } from 'react';
import { Link } from 'react-router-dom';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Image from 'react-bootstrap/Image'

class NotFound extends Component {
	render() {
		return (
			<Container>
				<Row className="justify-content-md-center">
					<h1><b>Page Not Found.</b></h1>
				</Row>
				<hr />
				<Row className="justify-content-md-center">	
					<h3>But I hope you enjoy a picture of my puppy Moose!</h3>
				</Row>
				<Row className="justify-content-md-center">
					<Image title="Baby Moose" width={300} height={350}src="https://nigelhaney.me/imgs/cutemoose.jpg" />
				</Row>
				<br />
				<Row className="justify-content-md-center">
					<Link to="/">Return to home page</Link>
				</Row>
			</Container>
		);
	}
}


export default NotFound;
