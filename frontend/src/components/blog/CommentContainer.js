import React, { Component } from 'react';
import PropTypes from 'prop-types';
import axios from 'axios';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import Comment from './Comment';
import AddCommentForm from './AddCommentForm';
import Loader from 'react-loader-spinner';

class CommentContainer extends Component {
	_isMounted = false;
	
	constructor(props) {
		super(props);

		this.state = {
			comments: [],
			isLoading: true,
			needsUpdate: false
		};

		this.commentChangeHandler = this.commentChangeHandler.bind(this);
	};

	commentChangeHandler(new_comment) {
		if (this._isMounted) {
			this.setState({comments:this.state.comments.concat([new_comment]),
					   isLoading: true, needsUpdate:true});
		}
	};

	componentWillMount() {
		this._isMounted = true;

		axios.get("https://nigelhaney.me/api/blog/comments/" + this.props.post_id)
			.then(res => {
			if (this._isMounted) {
				this.setState({comments: res.data.data,
						   isLoading: false});
			}
		});
	};

	componentDidUpdate() {
		// console.log("here");
		if (this.state.needsUpdate){
				axios.get("https://nigelhaney.me/api/blog/comments/" + this.props.post_id)
				.then(res => {
					// console.log(res.data.data);
				if (this._isMounted) {
					this.setState({comments: res.data.data,
								   isLoading: false,
								   needsUpdate: false});
				}
			});
		}
		
	}

	componentWillUnmount() {
		this._isMounted = false;
	};

	render() {
		return (
			<Container>
				<Row>
					<Col>
						<h2>Comments ({this.state.comments.length}):</h2>
					</Col>
				</Row>
				<hr />
				{this.state.isLoading &&
					<Container>
						<Row>
							<h3>Loading comments...</h3>
						</Row>
						<Row className="justify-content-md-center">
							<Loader type="TailSpin" color="#000" height="75" width="75"/>
						</Row>
					</Container>
				}
				{!this.state.isLoading &&
					<Container>
						{
							this.state.comments.map((item, i) => {
								return(
									<Row key={item.comment_id}>
										<Comment item={item} />
										<hr />
									</Row>
								)
							})
						}
						<hr />
						<Row>
							<AddCommentForm post_id={this.props.post_id} changeHandler={this.commentChangeHandler} />
						</Row>
					</Container>
				}
			</Container>
		);
	};
}

CommentContainer.propTypes = {
	post_id: PropTypes.number.isRequired
}


export default CommentContainer;
