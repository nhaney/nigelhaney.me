import React, { Component } from 'react';
import axios from 'axios';
import { Link }  from 'react-router-dom';

import CommentContainer from './CommentContainer';
import MailListContainer from './MailListContainer';
import dateConverter from '../../utils/utils';

import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';


class BlogPost extends Component {
	
	constructor(props) {
		super(props);

		this.state = {
			post_info: [],
			isLoading: true,
			hasErrored: false
		};
	}

	componentWillMount(){
		// console.log(this.props.match);
		// if we are coming from blog preview page, we already have post info
		if (this.props.location.state) {
			// console.log("Info already found.");
			this.setState({
				post_info:this.props.location.state.item,
				isLoading:false
			});
			return;
		}

		const post_title = this.props.match.params.post_title;
		axios.get("https://nigelhaney.me/api/blog/posts/" + post_title)
		.then(res => {
			this.setState({post_info: res.data.data,
						   isLoading: false});
		})
		.catch(res => {
			// console.log(res.response)
			this.setState({isLoading: false,
						   hasErrored: true,
						   post_info: res.response.data});
		});
	}

	render() {
		// console.log(this.state.post_info);
		let published_date = dateConverter(this.state.post_info.published_time);
		let edited_date = "";
		if (this.state.post_info.last_edited) {
			edited_date = dateConverter(this.state.post_info.last_edited);
		}

		return (
				<Container>
					{this.state.isLoading && 
						<h1 style={{textAlign:"center"}}>Loading...</h1>
					}
					{this.state.hasErrored && 
						<Container>
							<h1 style={{textAlign:"center"}}>{this.state.post_info.message}</h1>
							<Link to="/blog">
								<h3 style={{textAlign:"center"}}>Click here to return to blog</h3>
							</Link>
						</Container>
					}
					{!this.state.isLoading && !this.state.hasErrored &&
						<Container>
							<Row className="justify-content-md-center">
								<Col />
								<Col>
									<h1 style={{textAlign:"center"}}>{this.state.post_info.post_title}</h1>
								</Col>
								<Col>
									<p style={{textAlign:"right"}}><i>Posted by Nigel on {published_date}<br />
									{this.state.post_info.last_edited && "Last edited on " + edited_date}</i></p>
								</Col>
							</Row>
							<hr />
							<Row dangerouslySetInnerHTML={{__html: this.state.post_info.content}} />
							<hr />
							<Row>
								<CommentContainer post_id={this.state.post_info.post_id} />
							</Row>
							<Row>
								<MailListContainer />
							</Row>
						</Container>
					}
				</Container>
		);
	}
}

export default BlogPost;