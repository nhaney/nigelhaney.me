import React, { Component } from 'react';
import axios from 'axios';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import Loader from 'react-loader-spinner';

class MailListContainer extends Component {
	constructor(props) {
		super(props);

		this.state = {
			email: "",
			isSubmitting: false,
			hasSubmitted: false,
			errorMessage: ""
		}
		
		this.handleChange = this.handleChange.bind(this);
		this.subscribe = this.subscribe.bind(this);
	}

	handleChange(event) {
		this.setState({email: event.target.value});
	}

	subscribe(event, email) {
		event.preventDefault();

		this.setState({isSubmitting: true});
		axios.post("https://nigelhaney.me/api/mail/subscribe",
							{ "email": this.state.email })
							.then(res => {
									this.setState({hasSubmitted: true});
									// console.log(this.state)
							})
							.catch(error => {
								this.setState({isSubmitting:false, errorMessage:error.response.data.message})
							});
	}

	render() {
		return (
				<Container>
					{!this.state.hasSubmitted &&
						<Container style={{padding:"30px"}}>
							<Row className="justify-content-md-center">
								<Col md={4}>
									<h4 style={{textAlign:"center"}}>Sign up for my mailing list!</h4>
									<p style={{textAlign:"center"}}>You will be notified whenever I make a new blog post</p>
								</Col>
							</Row>
							<Row className="justify-content-md-center">
								<Col md={4}>
									<Form onSubmit={this.subscribe}>
										<Form.Control disabled={this.state.isSubmitting} type="email" placeholder="Enter your email here" onChange={this.handleChange} />
										<Form.Text className="text-muted">
											No spam, I promise. You may unsubscribe at any time.
										</Form.Text>
									</Form>
								</Col>
								<Col md={2}>
									<Button disabled={this.state.isSubmitting} variant="primary" onClick={this.subscribe}>
										{!this.state.isSubmitting && "Sign up!"}
										{this.state.isSubmitting && 
											<Loader type="TailSpin" color="#fff" height="20" width="20"/>
										}
									</Button>
									<p style={{color:"red"}}>{this.state.errorMessage}</p>
								</Col>
							</Row>
						</Container>
					}
					{this.state.hasSubmitted &&
						<Container style={{border:"1px solid black"}}>
							<Row className="justify-content-md-center">
								<h4 style={{color:"green"}}>
									Confirmation email sent to {this.state.email}. Thanks for your interest!
								</h4>
							</Row>
						</Container>
					}
				</Container>
		);
	}
}

export default MailListContainer;