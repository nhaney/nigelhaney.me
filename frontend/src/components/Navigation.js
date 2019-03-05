import React, { Component } from 'react';
import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import '../styles/navigation.css'

class Navigation extends Component {
  render() {
  		return (
  			<Navbar expand="sm" sticky="top" bg="dark" variant="dark">
  				<Navbar.Toggle aria-controls="basic-navbar-nav" />
  				<Navbar.Collapse className="justify-content-center" id="basic-navbar-nav">
						<Nav >
								<Nav.Item>
									<Nav.Link href="/" style={navStyle}>Home</Nav.Link>
								</Nav.Item>
								<Nav.Item>
									<Nav.Link href="/about" style={navStyle}>About</Nav.Link>
								</Nav.Item>
								<Nav.Item>
									<Nav.Link href="/blog" style={navStyle}>Blog</Nav.Link>
								</Nav.Item>
								<Nav.Item>
									<Nav.Link href="/experience" style={navStyle}>Experience</Nav.Link>
								</Nav.Item>
								<Nav.Item>
									<Nav.Link href="/games" style={navStyle}>Games</Nav.Link>
								</Nav.Item>
						</Nav>
				</Navbar.Collapse>
			</Navbar>
  		);
  	}
}

const navStyle = {
	paddingLeft: "30px",
	paddingRight: "30px"
}

export default Navigation;