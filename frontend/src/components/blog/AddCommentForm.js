import React, { Component } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';

import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button'; 
import Container from 'react-bootstrap/Container';
import Loader from 'react-loader-spinner';

class AddCommentForm extends Component {
	constructor(props) {
		super(props);

		this.state = {
			author: "",
			content: "",
			needsAuthor: false,
			needsContent: false,
			isWaiting: false,
			hasErrored: false,
			errorMessage: ""
		};
		this.handleChange = this.handleChange.bind(this);
		this.handleSubmit = this.handleSubmit.bind(this);
	};

	handleChange(event) {
		this.setState({[event.target.name]: event.target.value});
	};

	handleSubmit(event) {
		event.preventDefault();

		var authorCheck = false;
		var contentCheck = false;

		if (this.state.author === "") {
			authorCheck = true
		}

		if (this.state.content === "") {
			contentCheck = true
		}

		if (authorCheck || contentCheck) {
			this.setState({
				needsAuthor: authorCheck,
				needsContent: contentCheck
			});
			return
		}

		axios.post("https://nigelhaney.me/api/blog/comments", 
				  { "author": this.state.author,
			  		"content": this.state.content,
			  		"post_id": this.props.post_id})
			.then(res => {
				// console.log(res);
			  	this.props.changeHandler(res);
			  })
			.catch(error => {
				this.setState({hasErrored: true, errorMessage: error.response.data.message})
			})
	};

	render() {
		return (
			<Container>
				<h2>Leave a comment!</h2>
				<Form onSubmit={this.handleSubmit}>
					<Form.Group controlId="author">
						<Form.Label>Name:</Form.Label>
						<Form.Control type="text" placeholder="Enter your name"
									  name="author" 
									  onChange={this.handleChange} />
						<Form.Text style={{color:"red"}}>
							{ this.state.needsAuthor && "Name required" }
						</Form.Text>
					</Form.Group>
					<Form.Group controlId="content">
						<Form.Label>Comment:</Form.Label>
						<Form.Control as="textarea" rows="5"
									  placeholder="Enter your comment"
									  name="content"
									  onChange={this.handleChange} />
						<Form.Text style={{color:"red"}}>
							{ this.state.needsContent && "Comment required" }
						</Form.Text>
					</Form.Group>
					<Button variant="primary" type="submit">
						{!this.state.isWaiting && "Submit"}
						{this.state.isWaiting && <Loader type="TailSpin" color="#fff" height="20" width="20"/>}
					</Button>
					{this.state.hasErrored &&
						<Form.Label style={{margin:"10px", color:"red"}}><b>{this.state.errorMessage}</b></Form.Label>
					}
				</Form>
				<hr />
			</Container>
		);
	}
}

AddCommentForm.propTypes = {
	post_id: PropTypes.number.isRequired,
	changeHandler: PropTypes.func.isRequired
}

export default AddCommentForm;