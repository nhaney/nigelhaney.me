import React, { Component } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import '../styles/footer.css'


class Footer extends Component {
	render() {
		return (
			<footer>
				<Container>
					<hr />
					<Row className="justify-content-md-center">
						<Col md={{span:4, offset:8}}>
							<p style={{"textAlign":"right"}}>Site made by Nigel Haney, 2019</p>
						</Col>
					</Row>
				</Container>
			</footer>
		);
	}
}

export default Footer