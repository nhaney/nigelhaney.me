import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

class Header extends Component {
	render() {
		return (
			<Container fluid={true} style={navigationStyle}>
				<Row>
					<Col sm={4} />
					<Col sm={4}>
						<a style={{textDecoration: "none"}} href="/">
							<h1 style={websiteHeaderStyle}><b>Nigel Haney</b></h1>
						</a>
					</Col>
					<Col sm={4} className="d-flex justify-content-end">
						<a href="https://github.com/nhaney" className="fa fa-github"> </a>
						<a href="https://www.linkedin.com/in/nigel-haney/" className="fa fa-linkedin"> </a>
						<a href="https://www.youtube.com/channel/UC8kot0jObfGnY28lYXmQugw" className="fa fa-youtube"> </a>
					</Col>
				</Row>
			</Container>
		);
	}
}

const navigationStyle = {
	backgroundColor: '#f4f4f4',
	width: "100%"
}

const websiteHeaderStyle = {
	"textAlign": "center",
	"fontFamily":"Helvetica",
	"fontSize":"60px",
	"color":"#353B41",
}

export default Header;
